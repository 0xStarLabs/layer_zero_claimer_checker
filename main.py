import sys
import time
import ccxt
import random
import urllib3
import itertools
from web3 import Web3
from loguru import logger
from eth_account import Account
from itertools import cycle
from checker import Checker
from common import read_wallets
from concurrent.futures import ThreadPoolExecutor
from constants import ERC20_ABI, ZRO_ABI, ZRO_DONATE_ABI, RPCS
from config import OKX_API_KEY, OKX_API_SECRET, OKX_API_PASSPHRASE, MODULES
import threading

TOTAL_ZRO = 0
PRIVATE_KEYS = []
private_keys_lock = threading.Lock()  # Add this line
token_contract_address = "0x6985884C4392D348587B19cb9eAAf157F13271cd"
claim_contract_addresses = "0xB09F16F625B363875e39ADa56C03682088471523"
donate_contract_address = "0xd6b6a6701303B5Ea36fa0eDf7389b562d8F894DB"

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/arbitrum"))
token_contract = w3.eth.contract(address=Web3.to_checksum_address(token_contract_address), abi=ERC20_ABI)
claim_contract =  w3.eth.contract(address=Web3.to_checksum_address(claim_contract_addresses), abi=ZRO_ABI)
donate_contract = w3.eth.contract(address=Web3.to_checksum_address(donate_contract_address), abi=ZRO_DONATE_ABI)

def configuration():
    urllib3.disable_warnings()
    logger.remove()
    logger.add(sys.stdout, colorize=True,
               format="<light-cyan>{time:HH:mm:ss}</light-cyan> | <level> {level: <8}</level> | - <white>{"
                      "message}</white>")

def save_private_keys(private_keys):
    with open("./data/unclaimed_private_keys.txt", "w") as file:
        for key in private_keys:
            file.write(key + "\n")

rpc_cycle = cycle(RPCS)

def get_next_rpc():
    return next(rpc_cycle)
    
def get_web3():
    return Web3(Web3.HTTPProvider(get_next_rpc()))
   
def check_balance(address):
    w3 = get_web3()  # Get a Web3 instance with the next RPC
    balance = w3.eth.get_balance(Web3.to_checksum_address(address))
    balance_ether = w3.from_wei(balance, 'ether')
    return balance_ether

def get_amount_to_donate(amount_wei):
    l0_gas_response = donate_contract.functions.requiredDonation(amount_wei).call()
    return int(l0_gas_response[2])

def withdraw(address, amount_to_donate):
    try:
        # Initialize the OKX exchange
        exchange = ccxt.okx({
            'apiKey': OKX_API_KEY,
            'secret': OKX_API_SECRET,
            'password': OKX_API_PASSPHRASE,
            'enableRateLimit': True,
        })
        initial_balance = check_balance(address)
        amount_to_donate_ether = float(w3.from_wei(amount_to_donate, 'ether'))
        if initial_balance < amount_to_donate_ether:
            # Set up withdrawal parameters
            currency = 'ETH'
            amount = round(amount_to_donate_ether + 0.0005, random.randint(8, 12))
            if amount < 0.00104:
                amount = round(0.00104 + random.uniform(0.0001, 0.00002), random.randint(8, 12))
            network = 'Arbitrum One'  # Specify the network for Arbitrum

            # Perform the withdrawal
            result = exchange.withdraw(currency, amount, address, {
                'network': network,
                'fee': 0.00004,  # Adjust the fee as needed
            })

            logger.success(f"Withdrawal initiated: {amount} {currency} to {address}")
            logger.info(f"Transaction ID: {result['id']}")

            # Wait for funds to arrive
            max_wait_time = 600  # 10 minutes
            start_time = time.time()
            while time.time() - start_time < max_wait_time:
                current_balance = check_balance(address)
                if current_balance > initial_balance:
                    logger.success(f"Funds received. New balance: {current_balance} ETH")
                    return
                time.sleep(10)  # Check every 10 seconds

            logger.warning("Timeout waiting for funds to arrive. Proceeding with current balance.")
        else:
            logger.info(f"Sufficient balance already present: {initial_balance} ETH")

    except Exception as e:
        logger.error(f"Withdrawal failed: {str(e)}")


def claim(account: Account, private_key, amount_wei, amount_to_donate, proof):
    retries = 0
    max_retries = 5

    while retries < max_retries:
        try:
            if not proof:
                logger.error(f"Failed to get proof for {account.address}")
                return
            
            # Prepare the transaction
            transaction = claim_contract.functions.donateAndClaim(
                2,
                amount_to_donate,
                amount_wei,
                proof,  # Pass the proof as-is, it's already a list of hashes
                account.address,
                b""  # Empty bytes for the last argument
            )

            # Estimate gas and prepare transaction parameters
            gas_estimate = transaction.estimate_gas({'from': account.address, 'value': amount_to_donate})
            gas_limit = int(gas_estimate * random.uniform(1.2, 1.3))  # Add 20% buffer
            nonce = w3.eth.get_transaction_count(account.address)

            # Build the transaction
            txn = transaction.build_transaction({
                'chainId': 42161,  # Arbitrum chain ID
                'gas': gas_limit,
                'maxFeePerGas': w3.eth.max_priority_fee + (2 * w3.eth.get_block('latest')['baseFeePerGas']),
                'maxPriorityFeePerGas': w3.eth.max_priority_fee,
                'nonce': nonce,
                'value': amount_to_donate
            })
            
            # Sign and send the transaction
            signed_txn = w3.eth.account.sign_transaction(txn, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            
            # Wait for the transaction to be mined
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            
            amount_ether = w3.from_wei(amount_wei, 'ether')
            logger.success(f"Claimed {amount_ether:.6f} ZRO for {account.address}")
            logger.info(f"Transaction hash: {tx_hash.hex()}")
            return  # Success, exit the function
        except Exception as e:
            retries += 1
            logger.warning(f"Error during claim (attempt {retries}/{max_retries}): {e}")
            if retries < max_retries:
                time.sleep(random.uniform(3, 9))  # Wait before retrying
            else:
                logger.exception(f"Max retries reached. Claim failed for {account.address}")


def send(account: Account, deposit_address, private_key):
    retries = 0
    max_retries = 5

    while retries < max_retries:
        try:
            amount = token_contract.functions.balanceOf(Web3.to_checksum_address(account.address)).call()
            if amount > 0:
                # Prepare the transaction
                transaction = token_contract.functions.transfer(Web3.to_checksum_address(deposit_address), amount)
                
                # Estimate gas for the transaction
                estimated_gas = transaction.estimate_gas({'from': account.address})
                gas_limit = int(estimated_gas * random.uniform(1.2, 1.3))  # Increase the gas estimate by up to 30%

                nonce = w3.eth.get_transaction_count(account.address)
                txn = transaction.build_transaction({
                    'chainId': 42161,
                    'gas': gas_limit,
                    'maxFeePerGas': w3.eth.max_priority_fee + (2 * w3.eth.get_block('latest')['baseFeePerGas']),
                    'maxPriorityFeePerGas': w3.eth.max_priority_fee,
                    'nonce': nonce,
                })

                signed_txn = w3.eth.account.sign_transaction(txn, private_key)
                txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                logger.success(f" {deposit_address} | Sent Transaction: https://arbiscan.io/tx/{txn_hash.hex()}")
                time.sleep(random.randint(5, 15))
                return  # Success, exit the function
            else:
                logger.info(f" {deposit_address} | No tokens")
                return  # No tokens, exit the function
        except Exception as e:
            retries += 1
            logger.warning(f"Error during send (attempt {retries}/{max_retries}): {e}")
            if retries < max_retries:
                time.sleep(random.uniform(3, 9))  # Wait before retrying
            else:
                logger.error(f"Max retries reached. Send failed for {account.address} to {deposit_address}")


def process_account(private_key, deposit_address, proxy, i):
    account = Account.from_key(private_key)
    logger.info(f"{i} | Checking {account.address} deposit to: {deposit_address}")
    checker = Checker(account, proxy)  # Checker class will handle None proxy
    proof, amount_1, amount_2 = checker.get_proof()
    if proof:
        amount_1 = int(amount_1)
        amount_2 = int(amount_2)
        amount_full = int(amount_1 + amount_2)
        amount_2_ether = w3.from_wei(amount_2, 'ether')
        logger.success(f"{i} | {account.address} Claiming {amount_2_ether} ZRO")
        amount_to_donate = get_amount_to_donate(amount_2)
        amount_to_donate_buffer = int(amount_to_donate * 1.02)
        amount_to_donate_ether = w3.from_wei(amount_to_donate_buffer, 'ether')
        balance_ether = check_balance(account.address)
        global TOTAL_ZRO
        with private_keys_lock:  # Use a lock when modifying shared resources
            TOTAL_ZRO += amount_2_ether
            PRIVATE_KEYS.append(private_key)
        
        if "Withdraw" in MODULES and balance_ether < amount_to_donate_ether:
            withdraw(account.address, amount_to_donate)
            time.sleep(random.randint(5, 10))

        if "Claim" in MODULES:
            claim(account, private_key, amount_full, amount_to_donate, proof)
            time.sleep(random.randint(5, 10))

        if "Send" in MODULES:
            send(account, deposit_address, private_key)
    
    print('\n')
    time.sleep(random.randint(3, 5))


def main():
    private_keys, deposit_addresses, proxies = read_wallets()
    logger.success(f"Loaded Private Keys: {len(private_keys)} | Deposit Addresses: {len(deposit_addresses)}")
    num_threads = int(input("Enter the number of threads to use: "))

    # Create a list of tasks
    tasks = list(enumerate(zip(private_keys, deposit_addresses, itertools.cycle(proxies or [None])), 1))
    
    # Use ThreadPoolExecutor to run tasks concurrently
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(lambda x: process_account(*x[1], x[0]), tasks)
    logger.success(f"Total ZRO: {TOTAL_ZRO}")
    save_private_keys(PRIVATE_KEYS)

if __name__ == "__main__":
    configuration()
    main()

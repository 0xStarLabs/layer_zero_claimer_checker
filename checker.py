import requests
from web3 import Web3
from eth_abi import encode
from random import choice
from constants import HEADERS, RPCS
from loguru import logger

class Checker:
    def __init__(self, account, proxy=None):
        self.account = account
        self.session = requests.Session()
        if proxy:
            if proxy:
                self.session.proxies.update({
                    'http': "http://" + proxy,
                    'https': "http://" + proxy
                })

    def check_eligible(self):
        url = f'https://www.layerzero.foundation/api/allocation/{self.account.address}'
        response = self.session.get(url, headers=HEADERS)
        response_json = response.json()
        if 'isEligible' in response_json:
            return response_json['isEligible'], response_json['zroAllocation']['asString'], response_json['zroAllocation']['asBigInt']
        elif response_json.get('error') == 'Record not found':
            return False, None, None
        else:
            print(f'{self.account.address} | Unexpected Response When Checking Eligible: {response.text}')
            return False, None, None

    def check_claimed_amount(self):
        url = choice(RPCS)
        payload = {
            'id': 1,
            'jsonrpc': '2.0',
            'method': 'eth_call',
            'params': [{
                'to': '0xd6b6a6701303b5ea36fa0edf7389b562d8f894db',
                'data': '0x7a692982' + encode(['address'], [Web3.to_checksum_address(self.account.address)]).hex()
            }]
        }
        response = self.session.post(url, json=payload)
        response_json = response.json()
        claimed_amount = int(response_json['result'], 16)
        return claimed_amount > 0

    def get_proof(self, address):
        try:
            proof_response = self.session.get(f'https://www.layerzero.foundation/api/proof/{address}', headers=HEADERS)
            if not proof_response.ok:
                logger.error(f'Failed to get proof for {address}: {proof_response.text}')
                return None

            proof_json = proof_response.json()
            proof = proof_json['proof'].split('|')
            return proof
        
        except Exception as e:
            logger.error(f"Error getting proof: {e}")
            return None

    def check_account(self):
        is_eligible, amount, amount_bigint = self.check_eligible()

        if not is_eligible:
            logger.info(f'{self.account.address} | Not Eligible')
            return None, None, None

        is_claimed = self.check_claimed_amount()

        if is_claimed:
            logger.info(f'{self.account.address} | {amount} Claimed')
            return None, None, None
        
        logger.success(f'{self.account.address} | {amount} Claimable')
        
        proof = self.get_proof(self.account.address)

        return float(amount), amount_bigint, proof


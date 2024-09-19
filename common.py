import re
import random
from eth_utils import is_address

def read_wallets():
    private_keys = []
    addresses = []
    proxies = []

    # Read and verify private keys
    with open("./data/private_keys.txt", 'r') as file:
        for line in file:
            key = line.strip()
            if re.match(r'^(0x)?[a-fA-F0-9]{64}$', key):
                private_keys.append(key if key.startswith('0x') else '0x' + key)
            # else: consider logging invalid keys

    # Read and verify deposit addresses
    with open("./data/deposit_addresses.txt", 'r') as file:
        for line in file:
            addr = line.strip()
            if is_address(addr):
                addresses.append(addr)
            # else: consider logging invalid addresses

    # Read and process proxies
    with open("./data/proxies.txt", 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]

    if not proxies:
        proxies = None
    elif len(proxies) < len(private_keys):
        proxies = proxies + random.choices(proxies, k=len(private_keys) - len(proxies))

    return private_keys, addresses, proxies

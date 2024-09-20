import requests
from web3 import Web3
from eth_abi import encode
from random import choice
from constants import HEADERS, RPCS
from loguru import logger

class Checker:
    def __init__(self, account, proxy=None):
        try:
            self.account = account
            self.session = requests.Session()
            if proxy:
                self.session.proxies.update({
                    'http': "http://" + proxy,
                    'https': "http://" + proxy
                })
        except requests.exceptions.RequestException as e:
            logger.error(f"Error initializing Checker: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in Checker initialization: {e}")
            raise

    # def check_claimed_amount(self):
    #     try:
    #         url = choice(RPCS)
    #         payload = {
    #             'id': 1,
    #             'jsonrpc': '2.0',
    #             'method': 'eth_call',
    #             'params': [{
    #                 'to': '0xd6b6a6701303b5ea36fa0edf7389b562d8f894db',
    #                 'data': '0x7a692982' + encode(['address'], [Web3.to_checksum_address(self.account.address)]).hex()
    #             }]
    #         }
    #         response = self.session.post(url, json=payload)
    #         response.raise_for_status()
    #         response_json = response.json()
    #         claimed_amount = int(response_json['result'], 16)
    #         return claimed_amount > 0
    #     except requests.exceptions.RequestException as e:
    #         logger.error(f'check_claimed_amount: Request error: {e}')
    #         return False
    #     except Exception as e:
    #         logger.error(f'check_claimed_amount: Unexpected error: {e}')
    #         return False

    def get_proof(self):
        try:
            proof_response = self.session.get(f'https://www.layerzero.foundation/api/proof/{self.account.address}', headers=HEADERS)
            proof_response.raise_for_status()
            proof_json = proof_response.json()
            proof = proof_json['proof'].split('|')
            amount_1 = int(proof_json['round1'])
            amount_2 = int(proof_json['round2'])
            return proof, amount_1, amount_2
        except requests.exceptions.RequestException as e:
            # logger.error(f'get_proof: Request error: {e}')
            logger.info(f'{self.account.address} | No second allocation')
            return None, None, None
        except Exception as e:
            logger.error(f'get_proof: Unexpected error: {e}')
            return None, None, None


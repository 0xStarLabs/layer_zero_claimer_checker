## Software for an automatic layer zero airdrop allocation claim, check and transfer.
## Софт для автоматического чека, клейма и траснфера аирдропа лейер зиро.


## 🔗 Links
[![Telegram channel](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/StarLabsTech)](https://t.me/StarLabsTech)
[![Telegram chat](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/StarLabsChat)](https://t.me/StarLabsChat)

🔔 CHANNEL: https://t.me/StarLabsTech

💬 CHAT: https://t.me/StarLabsChat

💰 DONATION EVM ADDRESS: 0x620ea8b01607efdf3c74994391f86523acf6f9e1

## 🤖 | Features :

🟢 Checker

🟢 Withdraw

🟢 Claim

🟢 Send

## ⚙️ Config

| Name | Description |
| --- | --- |
| Modules | Choose the modules you need. The checker will run by default. If you only need the checker, you can remove the rest. |
| OKX_API_KEY | API key used to withdraw ETH from OKX. |
| OKX_API_SECRET | API secret key used to withdraw ETH from OKX. |
| OKX_API_PASSPHRASE | Passphrase for your OKX account. |


## 🚀 Installation
git clone https://github.com/0xStarLabs/layer_zero_claimer_checker.git

pip install -r requirements.txt


## 🗂️ Data

| Name | Description |
| --- | --- |
| deposit_addresses.txt | List of addresses where ZRO will be deposited (Optional, required only if ZRO deposits are needed).|
| private_keys.txt | Private keys of the wallets that will be used to claim ZRO. |
| proxies.txt | Proxies to prevent all requests from being sent to the LayerZero website from the same IP (Optional). |

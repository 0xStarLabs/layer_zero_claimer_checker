RPCS = [
    "https://arbitrum-one-rpc.publicnode.com", 
    "https://arbitrum-one.public.blastapi.io",
    "https://arbitrum.meowrpc.com", 
    "https://arbitrum.drpc.org", 
    "https://arbitrum.llamarpc.com",
    "https://rpc.ankr.com/arbitrum" 
]

HEADERS = {
    'accept': 'application/json',
    'accept-language': 'uk',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

ERC20_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {"name": "", "type": "string"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_spender", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [
            {"name": "", "type": "bool"}
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {"name": "", "type": "uint256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_from", "type": "address"},
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transferFrom",
        "outputs": [
            {"name": "", "type": "bool"}
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {"name": "", "type": "uint8"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_owner", "type": "address"}
        ],
        "name": "balanceOf",
        "outputs": [
            {"name": "balance", "type": "uint256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {"name": "", "type": "string"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [
            {"name": "", "type": "bool"}
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_owner", "type": "address"},
            {"name": "_spender", "type": "address"}
        ],
        "name": "allowance",
        "outputs": [
            {"name": "", "type": "uint256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {"name": "_from", "type": "address"},
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {"name": "_owner", "type": "address"},
            {"name": "_spender", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "Approval",
        "type": "event"
    }
]

ZRO_ABI = [{'inputs': [{'internalType': 'address', 'name': '_zroToken', 'type': 'address'}, {'internalType': 'address', 'name': '_endpoint', 'type': 'address'}, {'internalType': 'bytes32', 'name': '_merkleRoot', 'type': 'bytes32'}, {'internalType': 'address', 'name': '_donateContract', 'type': 'address'}, {'internalType': 'address', 'name': '_stargateUsdc', 'type': 'address'}, {'internalType': 'address', 'name': '_stargateUsdt', 'type': 'address'}, {'internalType': 'address', 'name': '_stargateNative', 'type': 'address'}, {'internalType': 'uint256', 'name': '_nativePrice', 'type': 'uint256'}, {'internalType': 'address', 'name': '_owner', 'type': 'address'}], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'inputs': [{'internalType': 'address', 'name': 'target', 'type': 'address'}], 'name': 'AddressEmptyCode', 'type': 'error'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'AddressInsufficientBalance', 'type': 'error'}, {'inputs': [{'internalType': 'address', 'name': 'user', 'type': 'address'}], 'name': 'AlreadyClaimed', 'type': 'error'}, {'inputs': [], 'name': 'DonateAndClaimAlreadySet', 'type': 'error'}, {'inputs': [], 'name': 'FailedInnerCall', 'type': 'error'}, {'inputs': [{'internalType': 'enum Currency', 'name': 'currency', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'expectedAmount', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'actualAmount', 'type': 'uint256'}], 'name': 'InsufficientDonation', 'type': 'error'}, {'inputs': [], 'name': 'InvalidDelegate', 'type': 'error'}, {'inputs': [], 'name': 'InvalidEndpointCall', 'type': 'error'}, {'inputs': [], 'name': 'InvalidNativeStargate', 'type': 'error'}, {'inputs': [], 'name': 'InvalidProof', 'type': 'error'}, {'inputs': [{'internalType': 'uint32', 'name': 'eid', 'type': 'uint32'}], 'name': 'NoPeer', 'type': 'error'}, {'inputs': [], 'name': 'OnlyDonateAndClaim', 'type': 'error'}, {'inputs': [{'internalType': 'address', 'name': 'addr', 'type': 'address'}], 'name': 'OnlyEndpoint', 'type': 'error'}, {'inputs': [{'internalType': 'uint32', 'name': 'eid', 'type': 'uint32'}, {'internalType': 'bytes32', 'name': 'sender', 'type': 'bytes32'}], 'name': 'OnlyPeer', 'type': 'error'}, {'inputs': [{'internalType': 'address', 'name': 'owner', 'type': 'address'}], 'name': 'OwnableInvalidOwner', 'type': 'error'}, {'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}], 'name': 'OwnableUnauthorizedAccount', 'type': 'error'}, {'inputs': [{'internalType': 'address', 'name': 'token', 'type': 'address'}], 'name': 'SafeERC20FailedOperation', 'type': 'error'}, {'inputs': [{'internalType': 'enum Currency', 'name': 'currency', 'type': 'uint8'}], 'name': 'UnsupportedCurrency', 'type': 'error'}, {'inputs': [], 'name': 'DENOMINATOR', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'components': [{'internalType': 'uint32', 'name': 'srcEid', 'type': 'uint32'}, {'internalType': 'bytes32', 'name': 'sender', 'type': 'bytes32'}, {'internalType': 'uint64', 'name': 'nonce', 'type': 'uint64'}], 'internalType': 'struct Origin', 'name': 'origin', 'type': 'tuple'}], 'name': 'allowInitializePath', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'enum Currency', 'name': '_currency', 'type': 'uint8'}, {'internalType': 'address', 'name': '_user', 'type': 'address'}, {'internalType': 'uint256', 'name': '_zroAmount', 'type': 'uint256'}], 'name': 'assertDonation', 'outputs': [], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_user', 'type': 'address'}, {'internalType': 'enum Currency', 'name': '_currency', 'type': 'uint8'}, {'internalType': 'uint256', 'name': '_zroAmount', 'type': 'uint256'}, {'internalType': 'bytes32[]', 'name': '_proof', 'type': 'bytes32[]'}, {'internalType': 'address', 'name': '_to', 'type': 'address'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'claim', 'outputs': [{'components': [{'internalType': 'bytes32', 'name': 'guid', 'type': 'bytes32'}, {'internalType': 'uint64', 'name': 'nonce', 'type': 'uint64'}, {'components': [{'internalType': 'uint256', 'name': 'nativeFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lzTokenFee', 'type': 'uint256'}], 'internalType': 'struct MessagingFee', 'name': 'fee', 'type': 'tuple'}], 'internalType': 'struct MessagingReceipt', 'name': 'receipt', 'type': 'tuple'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'enum Currency', 'name': '_currency', 'type': 'uint8'}, {'internalType': 'uint256', 'name': '_zroAmount', 'type': 'uint256'}, {'internalType': 'bytes32[]', 'name': '_proof', 'type': 'bytes32[]'}, {'internalType': 'address', 'name': '_to', 'type': 'address'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}], 'name': 'claim', 'outputs': [{'components': [{'internalType': 'bytes32', 'name': 'guid', 'type': 'bytes32'}, {'internalType': 'uint64', 'name': 'nonce', 'type': 'uint64'}, {'components': [{'internalType': 'uint256', 'name': 'nativeFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lzTokenFee', 'type': 'uint256'}], 'internalType': 'struct MessagingFee', 'name': 'fee', 'type': 'tuple'}], 'internalType': 'struct MessagingReceipt', 'name': 'receipt', 'type': 'tuple'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [{'internalType': 'enum Currency', 'name': 'currency', 'type': 'uint8'}, {'internalType': 'uint256', 'name': 'amountToDonate', 'type': 'uint256'}, {'internalType': 'uint256', 'name': '_zroAmount', 'type': 'uint256'}, {'internalType': 'bytes32[]', 'name': '_proof', 'type': 'bytes32[]'}, {'internalType': 'address', 'name': '_to', 'type': 'address'}, {'internalType': 'bytes', 'name': '_extraBytes', 'type': 'bytes'}], 'name': 'donateAndClaim', 'outputs': [{'components': [{'internalType': 'bytes32', 'name': 'guid', 'type': 'bytes32'}, {'internalType': 'uint64', 'name': 'nonce', 'type': 'uint64'}, {'components': [{'internalType': 'uint256', 'name': 'nativeFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lzTokenFee', 'type': 'uint256'}], 'internalType': 'struct MessagingFee', 'name': 'fee', 'type': 'tuple'}], 'internalType': 'struct MessagingReceipt', 'name': 'receipt', 'type': 'tuple'}], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'donateContract', 'outputs': [{'internalType': 'contract IDonate', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'endpoint', 'outputs': [{'internalType': 'contract ILayerZeroEndpointV2', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'components': [{'internalType': 'uint32', 'name': 'srcEid', 'type': 'uint32'}, {'internalType': 'bytes32', 'name': 'sender', 'type': 'bytes32'}, {'internalType': 'uint64', 'name': 'nonce', 'type': 'uint64'}], 'internalType': 'struct Origin', 'name': '', 'type': 'tuple'}, {'internalType': 'bytes', 'name': '', 'type': 'bytes'}, {'internalType': 'address', 'name': '_sender', 'type': 'address'}], 'name': 'isComposeMsgSender', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'components': [{'internalType': 'uint32', 'name': 'srcEid', 'type': 'uint32'}, {'internalType': 'bytes32', 'name': 'sender', 'type': 'bytes32'}, {'internalType': 'uint64', 'name': 'nonce', 'type': 'uint64'}], 'internalType': 'struct Origin', 'name': '_origin', 'type': 'tuple'}, {'internalType': 'bytes32', 'name': '_guid', 'type': 'bytes32'}, {'internalType': 'bytes', 'name': '_message', 'type': 'bytes'}, {'internalType': 'address', 'name': '_executor', 'type': 'address'}, {'internalType': 'bytes', 'name': '_extraData', 'type': 'bytes'}], 'name': 'lzReceive', 'outputs': [], 'stateMutability': 'payable', 'type': 'function'}, {'inputs': [], 'name': 'merkleRoot', 'outputs': [{'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint32', 'name': '', 'type': 'uint32'}, {'internalType': 'bytes32', 'name': '', 'type': 'bytes32'}], 'name': 'nextNonce', 'outputs': [{'internalType': 'uint64', 'name': 'nonce', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'numeratorNative', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'numeratorUsdc', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'numeratorUsdt', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'oAppVersion', 'outputs': [{'internalType': 'uint64', 'name': 'senderVersion', 'type': 'uint64'}, {'internalType': 'uint64', 'name': 'receiverVersion', 'type': 'uint64'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'owner', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint32', 'name': 'eid', 'type': 'uint32'}], 'name': 'peers', 'outputs': [{'internalType': 'bytes32', 'name': 'peer', 'type': 'bytes32'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'uint32', 'name': '_dstEid', 'type': 'uint32'}, {'internalType': 'uint256', 'name': '_zroAmount', 'type': 'uint256'}], 'name': 'quoteClaimCallback', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'nativeFee', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'lzTokenFee', 'type': 'uint256'}], 'internalType': 'struct MessagingFee', 'name': 'msgFee', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'renounceOwnership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint256', 'name': '_zroAmount', 'type': 'uint256'}], 'name': 'requiredDonation', 'outputs': [{'components': [{'internalType': 'uint256', 'name': 'usdc', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'usdt', 'type': 'uint256'}, {'internalType': 'uint256', 'name': 'native', 'type': 'uint256'}], 'internalType': 'struct Donation', 'name': '', 'type': 'tuple'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_delegate', 'type': 'address'}], 'name': 'setDelegate', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_donateAndClaim', 'type': 'address'}], 'name': 'setDonateAndClaim', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'bytes32', 'name': '_merkleRoot', 'type': 'bytes32'}], 'name': 'setMerkleRoot', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'uint32', 'name': '_eid', 'type': 'uint32'}, {'internalType': 'bytes32', 'name': '_peer', 'type': 'bytes32'}], 'name': 'setPeer', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'newOwner', 'type': 'address'}], 'name': 'transferOwnership', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': '_to', 'type': 'address'}, {'internalType': 'uint256', 'name': '_amount', 'type': 'uint256'}], 'name': 'withdrawZro', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [{'internalType': 'address', 'name': 'user', 'type': 'address'}], 'name': 'zroClaimed', 'outputs': [{'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'zroToken', 'outputs': [{'internalType': 'address', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}]

ZRO_DONATE_ABI = [{"inputs":[{"internalType":"address","name":"_zroToken","type":"address"},{"internalType":"address","name":"_endpoint","type":"address"},{"internalType":"bytes32","name":"_merkleRoot","type":"bytes32"},{"internalType":"address","name":"_donateContract","type":"address"},{"internalType":"address","name":"_stargateUsdc","type":"address"},{"internalType":"address","name":"_stargateUsdt","type":"address"},{"internalType":"address","name":"_stargateNative","type":"address"},{"internalType":"uint256","name":"_nativePrice","type":"uint256"},{"internalType":"address","name":"_owner","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"AddressEmptyCode","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"AddressInsufficientBalance","type":"error"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"AlreadyClaimed","type":"error"},{"inputs":[],"name":"DonateAndClaimAlreadySet","type":"error"},{"inputs":[],"name":"FailedInnerCall","type":"error"},{"inputs":[{"internalType":"enum Currency","name":"currency","type":"uint8"},{"internalType":"uint256","name":"expectedAmount","type":"uint256"},{"internalType":"uint256","name":"actualAmount","type":"uint256"}],"name":"InsufficientDonation","type":"error"},{"inputs":[],"name":"InvalidDelegate","type":"error"},{"inputs":[],"name":"InvalidEndpointCall","type":"error"},{"inputs":[],"name":"InvalidNativePrice","type":"error"},{"inputs":[],"name":"InvalidNativeStargate","type":"error"},{"inputs":[],"name":"InvalidProof","type":"error"},{"inputs":[],"name":"InvalidToAddress","type":"error"},{"inputs":[],"name":"MsgValueNotSupported","type":"error"},{"inputs":[{"internalType":"uint32","name":"eid","type":"uint32"}],"name":"NoPeer","type":"error"},{"inputs":[],"name":"OnlyDonateAndClaim","type":"error"},{"inputs":[{"internalType":"address","name":"addr","type":"address"}],"name":"OnlyEndpoint","type":"error"},{"inputs":[{"internalType":"uint32","name":"eid","type":"uint32"},{"internalType":"bytes32","name":"sender","type":"bytes32"}],"name":"OnlyPeer","type":"error"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"OwnableInvalidOwner","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"OwnableUnauthorizedAccount","type":"error"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"SafeERC20FailedOperation","type":"error"},{"inputs":[{"internalType":"enum Currency","name":"currency","type":"uint8"}],"name":"UnsupportedCurrency","type":"error"},{"inputs":[],"name":"WithdrawFailed","type":"error"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"claimer","type":"address"},{"indexed":False,"internalType":"uint256","name":"expectedAmount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"actualAmount","type":"uint256"},{"indexed":False,"internalType":"address","name":"to","type":"address"}],"name":"Claim","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"claimer","type":"address"},{"indexed":False,"internalType":"uint256","name":"expectedAmount","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"actualAmount","type":"uint256"},{"indexed":False,"internalType":"uint32","name":"dstEid","type":"uint32"},{"indexed":False,"internalType":"address","name":"to","type":"address"}],"name":"ClaimRemote","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"donateAndClaim","type":"address"}],"name":"DonateAndClaimSet","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"bytes32","name":"merkleRoot","type":"bytes32"}],"name":"MerkleRootSet","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"NativeWithdrawn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint32","name":"eid","type":"uint32"},{"indexed":False,"internalType":"bytes32","name":"peer","type":"bytes32"}],"name":"PeerSet","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"requester","type":"address"},{"indexed":False,"internalType":"uint256","name":"zroAmount","type":"uint256"},{"indexed":False,"internalType":"address","name":"to","type":"address"}],"name":"ZRORequested","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"ZroWithdrawn","type":"event"},{"inputs":[],"name":"DENOMINATOR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"uint32","name":"srcEid","type":"uint32"},{"internalType":"bytes32","name":"sender","type":"bytes32"},{"internalType":"uint64","name":"nonce","type":"uint64"}],"internalType":"struct Origin","name":"origin","type":"tuple"}],"name":"allowInitializePath","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"enum Currency","name":"_currency","type":"uint8"},{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_zroAmount","type":"uint256"}],"name":"assertDonation","outputs":[],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"enum Currency","name":"_currency","type":"uint8"},{"internalType":"uint256","name":"_zroAmount","type":"uint256"},{"internalType":"bytes32[]","name":"_proof","type":"bytes32[]"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"claim","outputs":[{"components":[{"internalType":"bytes32","name":"guid","type":"bytes32"},{"internalType":"uint64","name":"nonce","type":"uint64"},{"components":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"lzTokenFee","type":"uint256"}],"internalType":"struct MessagingFee","name":"fee","type":"tuple"}],"internalType":"struct MessagingReceipt","name":"receipt","type":"tuple"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"enum Currency","name":"_currency","type":"uint8"},{"internalType":"uint256","name":"_zroAmount","type":"uint256"},{"internalType":"bytes32[]","name":"_proof","type":"bytes32[]"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"claim","outputs":[{"components":[{"internalType":"bytes32","name":"guid","type":"bytes32"},{"internalType":"uint64","name":"nonce","type":"uint64"},{"components":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"lzTokenFee","type":"uint256"}],"internalType":"struct MessagingFee","name":"fee","type":"tuple"}],"internalType":"struct MessagingReceipt","name":"receipt","type":"tuple"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"donateAndClaim","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"donateContract","outputs":[{"internalType":"contract IDonate","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"endpoint","outputs":[{"internalType":"contract ILayerZeroEndpointV2","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"uint32","name":"srcEid","type":"uint32"},{"internalType":"bytes32","name":"sender","type":"bytes32"},{"internalType":"uint64","name":"nonce","type":"uint64"}],"internalType":"struct Origin","name":"","type":"tuple"},{"internalType":"bytes","name":"","type":"bytes"},{"internalType":"address","name":"_sender","type":"address"}],"name":"isComposeMsgSender","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"uint32","name":"srcEid","type":"uint32"},{"internalType":"bytes32","name":"sender","type":"bytes32"},{"internalType":"uint64","name":"nonce","type":"uint64"}],"internalType":"struct Origin","name":"_origin","type":"tuple"},{"internalType":"bytes32","name":"_guid","type":"bytes32"},{"internalType":"bytes","name":"_message","type":"bytes"},{"internalType":"address","name":"_executor","type":"address"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"lzReceive","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"merkleRoot","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32","name":"","type":"uint32"},{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"nextNonce","outputs":[{"internalType":"uint64","name":"nonce","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"numeratorNative","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"numeratorUsdc","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"numeratorUsdt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"oAppVersion","outputs":[{"internalType":"uint64","name":"senderVersion","type":"uint64"},{"internalType":"uint64","name":"receiverVersion","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32","name":"eid","type":"uint32"}],"name":"peers","outputs":[{"internalType":"bytes32","name":"peer","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32","name":"_dstEid","type":"uint32"},{"internalType":"uint256","name":"_zroAmount","type":"uint256"}],"name":"quoteClaimCallback","outputs":[{"components":[{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"uint256","name":"lzTokenFee","type":"uint256"}],"internalType":"struct MessagingFee","name":"msgFee","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_zroAmount","type":"uint256"}],"name":"requiredDonation","outputs":[{"components":[{"internalType":"uint256","name":"usdc","type":"uint256"},{"internalType":"uint256","name":"usdt","type":"uint256"},{"internalType":"uint256","name":"native","type":"uint256"}],"internalType":"struct Donation","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_delegate","type":"address"}],"name":"setDelegate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_donateAndClaim","type":"address"}],"name":"setDonateAndClaim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"_merkleRoot","type":"bytes32"}],"name":"setMerkleRoot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_eid","type":"uint32"},{"internalType":"bytes32","name":"_peer","type":"bytes32"}],"name":"setPeer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawNative","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdrawZro","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"zroClaimed","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"zroToken","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]
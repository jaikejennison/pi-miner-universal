from web3 import Web3, HTTPProvider
#INFURA_PROJECT_ID = ''
#INFURA_API_SECRET=''
#INFURA_PROVIDER_URI='https://mainnet.infura.io/v3/' + WEB3_INFURA_PROJECT_ID

#w3 = Web3(HTTPProvider(INFURA_PROVIDER_UR))
web3 = Web3(HTTPProvider('http://PiMiner64.local:8545'))
block = web3.eth.getBlock('latest')
balance = web3.eth.getBalance(web3.eth.accounts[0])

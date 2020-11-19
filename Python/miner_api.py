from web3_init import *

### E X A M P L E S ###

# https://web3py.readthedocs.io/en/stable
# web3.eth.getBlock('latest')
# web3.eth.getBlock('pending')
# web3.eth.filter('latest')
# web3.eth.filter('pending')
# web3.eth.blockNumber
# web3.eth.chainId
# web3.eth.defaultBlock
# web3.eth.defaultAccount
# web3.eth.generateGasPrice()
# web3.eth.gasPrice
# web3.eth.syncing
# web3.eth.coinbase
# web3.eth.mining
# web3.eth.hashrate
# web3.eth.accounts
# web3.eth.protocolVersion
# web3.eth.getBalance(web3.eth.accounts[0])
# web3.eth.getStorageAt('0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B', 0)
# web3.eth.getProof('0x6C8f2A135f6ed072DE4503Bd7C4999a1a17F824B', [0], 3391)
# web3.eth.getUncleByBlock(web3.eth.defaultBlock, 0)
# web3.eth.getUncleCount(testHash)
# web3.eth.getUncleByBlockNumberAndIndex
# web3.eth.getBlock(web3.eth.defaultBlock)
# web3.eth.getBlockTransactionCount(block.number)
# web3.eth.getTransactionsByAccount(web3.eth.accounts[0])
# web3.eth.getTransactionByBlock(46147, 0)
# web3.eth.getTransactionReceipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
# web3.eth.getTransactionCount('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')
# web3.eth.waitForTransactionReceipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
# web3.eth.sendTransaction({'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601', 'from': web3.eth.coinbase, 'value': 12345})
# web3.toWei(web3.eth.getBalance(web3.eth.accounts[0]), 'ether')
# web3.fromWei(web3.eth.getBalance(web3.eth.accounts[0]), 'ether')
# web3.eth.submitWork(nonce, pow_hash, mix_digest)
# web3.geth.miner.set_extra('abcdefghijklmnopqrstuvwxyzABCDEF')
# web3.geth.miner.set_gas_price(19999999999)
# web3.geth.miner.start(4)
# web3.geth.miner.stop()
# web3.geth.miner.start_auto_dag()
# web3.geth.miner.stop_auto_dag()
# web3.geth.miner.setEtherbase(web3.eth.accounts[0])
# web3.net.listening
# web3.net.peer_count
# web3.net.version
# web3.geth.admin.node_info()
# web3.geth.admin.peers()
# web3.geth.personal.list_accounts()
# web3.geth.personal.list_wallets()
# web3.geth.txpool.inspect()
# web3.geth.txpool.status()
# web3.geth.txpool.content()

#print("TITLE : {}".format(CODE))
#print("TITLE : {}".format(CODE))
#print("TITLE : {}".format(CODE))


def pi_miner():
    print("\nweb3.eth")
    print("--------")
    print("| Net: {} | Mining: {} | Net Listening: {} | Hash Rate: {} | Block: {} | Transaction: {} | Peers: {} |".format(
        web3.net.version,
        web3.eth.mining,
        web3.net.listening,
        web3.eth.hashrate,
        web3.eth.blockNumber,
        web3.eth.getBlockTransactionCount(web3.eth.blockNumber),
        web3.net.peer_count
    ))
    print("| Client: {} | Balance: {} | Ether From Wei: {} | Gwei From Wei: {} |".format(
        web3.clientVersion,
        balance,
        web3.fromWei(balance, 'ether'),
        Web3.fromWei(balance, 'gwei')
    ))
    print("| Sync: {} |".format(web3.toJSON(web3.eth.syncing)))
    print("\nweb3.toJSON(web3.eth.getBlock('latest')): {}".format(web3.toJSON(web3.eth.getBlock('latest'))))
    print("\nweb3.toJSON(web3.geth.shh.info()): {}".format(web3.toJSON(web3.geth.shh.info())))
    print("\nweb3.toJSON(web3.geth.admin.node_info()): {}".format(web3.toJSON(web3.geth.admin.node_info())))
    print("\nweb3.eth.getWork(): {}".format(web3.eth.getWork()))

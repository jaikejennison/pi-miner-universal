#! /bin/bash

# COMMANDS:
#   account		Manage accounts
#   attach		Start an interactive JavaScript environment
#   bug			opens a window to report a bug on the geth repo
#   console		Start an interactive JavaScript environment
#   copydb		Create a local chain from a target chaindata folder
#   dump		Dump a specific block from storage to config.toml
#   dumpconfig		Show configuration values
#   export		Export blockchain into file
#   export-preimages	Export the preimage database into an RLP stream
#   import		Import a blockchain file
#   import-preimages	Import the preimage database from an RLP stream
#   init		Bootstrap and initialize a new genesis block
#   js			Execute the specified JavaScript files
#   license		Display license information
#   monitor		Monitor and visualize node metrics
#   removedb		Remove blockchain and state databases
#   version		Print version numbers
#   wallet		Manage Ethereum presale wallets
#
# OPTIONS:
#   --config		TOML configuration file path
#   --pprof		Enable the profiling server on localhost
#   --pprofport "6060"	Profile server listening port
#   --metrics		Enable metrics collection and reporting
#   --shh		Enable Whisper
#   --ethstats value    Reporting URL of a ethstats service (nodename:secret@host:port)
#	Infura.io
#	PROJECT ID
#	71ec1650c49c46e2ac95dd41c35b783e
#	PROJECT SECRET
#	79636d3db3854964adc92515d11a4704
#	ENDPOINTS MAINNET
#	https://mainnet.infura.io/v3/71ec1650c49c46e2ac95dd41c35b783e
#	wss://mainnet.infura.io/ws/v3/71ec1650c49c46e2ac95dd41c35b783e
#	CODE
#	NODENAME="71ec1650c49c46e2ac95dd41c35b783e"
#	SECRET="79636d3db3854964adc92515d11a4704"
#	"$NODENAME:$SECRET@https://mainnet.infura.io:5001"
#   --fast
#   --lightkdf
#   --nodiscover
#   --verbosity=4
#   --mine
#   --miner.threads=4
#   --miner.etherbase "0"
#   --rpc --rpcaddr "0.0.0.0" --rpcport "8545"
#   --rpcvhosts "*" --rpccorsdomain "*" --rpcapi "$APIMODS"
#   --ws --wsaddr "0.0.0.0" --wsport "3334"
#   --wsorigins "*" --wsapi "$APIMODS"
#   --genesis "genesis.json"
#   --autodag
#   --cache=4096
#   --networkid "1"
#   --identity "nv83r"
# ################################################################ #
GETHBIN="/media/pi/PiDrive/bin"
DATADIR="/media/pi/PiDrive/src/geth"
APIADDR="0.0.0.0"
APIMODS="admin, db, debug, eth, miner, net, personal, shh, txpool, web3"
ACCOUNT="0x11c7aa4c66335be3b91ba35caded9aed58aa6c37"

"$GETHBIN/geth" \
	--networkid=1 \
	--miner.etherbase "$ACCOUNT" \
	--miner.extradata "0x2e3a3a6e5f763833723a3a2e" \
	--syncmode "fast" \
	--identity "0x6e76383372" \
	--datadir "$DATADIR" \
	--ethash.dagdir "$DATADIR/.ethash" \
	--rpc --rpcaddr "$APIADDR" --rpcport "8545" \
	--rpcvhosts "*" --rpccorsdomain "*" --rpcapi "$APIMODS" \
	--ws --wsaddr "$APIADDR" --wsport "3334" \
	--wsorigins "*" \
	--wsapi "$APIMODS" \
	--shh \
	--ipcpath "$DATADIR/geth.ipc" \
	--pprof --pprofaddr "$APIADDR" --pprofport "6060" \
	--metrics \
	--unlock "$ACCOUNT" \
	--password "$DATADIR/password" \
	console


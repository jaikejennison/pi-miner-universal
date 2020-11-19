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
#   --identity "0o0PiMiner640o0"
#   console
#   --identity "0x6e76383372"
#		Coinbase walett address 0xFE70ef07D329E7DfFe128b4F3dBCB55e916e3779
# ################################################################ #
ROOTDIR=`pwd`
GETHBIN="$ROOTDIR/bin"
DATADIR="$ROOTDIR/.ethereum"
DAGDIR="$ROOTDIR/.ethash"
APIADDR="0.0.0.0"
APIMODS="admin, db, debug, eth, miner, net, personal, shh, txpool, web3"
ACCOUNT="0x5cd9f5415a69c160e319cbe75db056f9374c98ca"
GPRICE="2500000000"
GLIMIT="8000071"
IDDATA="PiMiner64"
"$GETHBIN/geth" \
	--verbosity=3 \
	--networkid=1 \
	--datadir "$DATADIR" \
	--ethash.dagdir "$DAGDIR" \
	--miner.etherbase "$ACCOUNT" \
	--miner.threads=16 \
	--miner.gasprice "$GPRICE" \
	--miner.gaslimit "$GLIMIT" \
	--miner.gastarget "$GLIMIT" \
	--miner.extradata "$IDDATA" \
	--identity "$IDDATA" \
	--unlock "$ACCOUNT" \
	--password "$DATADIR/password" \
	--ipcpath "$DATADIR/geth.ipc" \
	--rpc \
	--rpcaddr "$APIADDR" \
	--rpcport "8545" \
	--rpcvhosts "*" \
	--rpccorsdomain "*" \
	--rpcapi "$APIMODS" \
	--ws \
	--wsaddr "$APIADDR" \
	--wsport "3334" \
	--wsorigins "*" \
	--wsapi "$APIMODS" \
	--shh \
	--pprof \
	--pprofaddr "$APIADDR" \
	--pprofport "6060" \
	--maxpeers "300" \
	--maxpendpeers "200" \
	--metrics

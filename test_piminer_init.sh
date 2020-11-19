#! /bin/bash

GETHBIN="/media/pi/PiDrive/bin"
DATADIR="/media/pi/PiDrive/src/geth"
APIMODS="admin,db,debug,eth,miner,net,personal,shh,txpool,web3"

"$GETHBIN/geth" \
	--extradata "0x2e3a3a6e5f763833723a3a2e" \
	--rpc --rpcaddr "0.0.0.0" --rpcport "8545" \
	--rpcvhosts "*" --rpccorsdomain "*" --rpcapi "$APIMODS" \
	--datadir "$DATADIR" \
	init "$DATADIR/genesis.json"

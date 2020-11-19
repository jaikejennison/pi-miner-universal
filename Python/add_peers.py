from web3_init import *
from nodes import node_arr

def add_peers():
    i = 0
    for peers in node_arr:
        i = i + 1
        peer_bool = web3.geth.admin.add_peer(peers)
        print("Peer # {}: {}".format(i, peers, peer_bool))
    print("[Added {} Peers of {} Total Peers]".format(i, len(node_arr)))

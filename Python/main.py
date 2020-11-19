from web3_init import *
from add_peers import add_peers
from collect import collect_data
from display import display_data
from miner_api import pi_miner
from ClassPiMoji import *
from time import sleep

i = 7199
while True:
    i = i + 1
    if i == 7200:
        i = 0
        add_peers()
    clear_hat()
    pi_miner()
    collect_data()
    display_data()
    ethereum_coin()
    sleep(60)

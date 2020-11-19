from web3_init import web3, block

def collect_data():
    data = str(block.totalDifficulty)
    file = open('data.txt', 'a')
    file.write(data)
    file.write('\n')
    file.close

import matplotlib.pyplot as plt
import numpy as np

def display_data():
    data = []
    file = open('data.txt', 'r')
    for line in file.read().splitlines():
        if line:
            data.append(float(line))
    file.close()
    fig, ax = plt.subplots()
    ax.plot(data, data, label='linear')
    ax.plot(data, np.power(data,2), label='quadratic')
    ax.plot(data, np.power(data,3), label='cubic')
    plt.xlabel('Unknown Value')
    plt.ylabel('Hash Difficulty')
    ax.legend()
    plt.savefig('chart.png')
    plt.cla()
    plt.clf()
    plt.close('all')


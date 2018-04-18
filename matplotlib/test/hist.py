# coding:utf-8

import matplotlib.pyplot as plt
import numpy as np

'''
test to plot hist gram
'''

def test_hist():

    data = [np.random.randint(0,n,n) for n in [3000,4000,5000]]
    labels = ['3k','4k','5k']
    bins = [0,100,500,1000,2000,3000,4000,5000]

    plt.hist(data,bins=bins,label=labels)
    plt.legend()

    plt.show()

def main():
    test_hist()

if __name__ == '__main__':
    main()
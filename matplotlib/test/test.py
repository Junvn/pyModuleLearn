# coding:utf-8


import matplotlib.pyplot as plt
import numpy as np

def test():
    data1 = np.arange(100,201)
    plt.plot(data1)
    plt.show()

def test_figure():
    data1 = np.arange(100,201)
    #print(data1)
    plt.plot(data1)

    data2 = np.arange(200,301)
    plt.figure()
    plt.plot(data2)

    data3 = np.arange(300,401)
    plt.figure()
    plt.plot(data3)

    plt.show()

def test_subplot():

    data1 = np.arange(100,201)
    #plt.subplot(3,1,1)
    plt.subplot(311)
    plt.plot(data1)

    data2 = np.arange(200,301)
    plt.subplot(3,1,2)
    plt.plot(data2)

    data3 = np.arange(300,401)
    plt.subplot(3,1,3)
    plt.plot(data3)

    plt.show()

if __name__ == '__main__':
    test_subplot()
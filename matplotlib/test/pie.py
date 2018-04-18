# coding:utf-8

import matplotlib.pyplot as plt
import numpy as np

'''
test to plot pie gram
'''

def test_pie():

    labels = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    data = np.random.rand(7)*100

    plt.pie(data,labels=labels,autopct='%1.1f%%')
    plt.axis('equal')
    plt.legend()

    plt.show()

def main():
    test_pie()

if __name__ == '__main__':
    main()
# coding:utf-8


import matplotlib.pyplot as plt


def test_plot():
    plt.plot([1,2,3],[3,6,9],'-r')
    plt.plot([1,2,3],[2,4,9],':g')

    plt.show()


def main():
    test_plot()


if __name__ == '__main__':
    main()

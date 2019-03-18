import math as m

import read


def func_1(matrix):
    """H(X)"""
    tmp=[sum(x) for x in zip(*matrix)]
    tmp_2=[m.log(i)*i for i in tmp]
    res = sum(tmp_2)
    return res*(-1)

def func_2(matrix):
    """H(Y)"""
    tmp = []
    for i in matrix:
        tmp.append(sum(i))
    tmp_2=[m.log(i)*i for i in tmp]
    res = sum(tmp_2)
    return res*(-1)

def main():
    s=read.readtxt('sa')
    print(func_1(s))
    print(func_2(s))

if __name__ == "__main__":
    main()


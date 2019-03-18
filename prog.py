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

def func_3(matrix):
    """H(XY)"""
    res = 0
    for i in matrix:
        for j in i:
           res += j*m.log(j)
    return res

def main():
    s=read.readtxt('sa')
    print(func_1(s))
    print(func_2(s))
    print(func_3(s))

if __name__ == "__main__":
    main()


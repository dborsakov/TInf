import math as m

import read


def func_1(matrix):
    """H(X)"""
    tmp=[sum(x) for x in zip(*matrix)]
    tmp_2 = [x*m.log(1/x,2) for x in tmp]
    res = sum(tmp_2)
    return res*(-1)

def func_2(matrix):
    """H(Y)"""
    tmp = []
    for i in matrix:
        tmp.append(sum(i))
    tmp_2=[m.log(1/i,2)*i for i in tmp]
    res = sum(tmp_2)
    return res*(-1)

def func_3(matrix):
    """H(XY)"""
    # res = 0
    # for i in matrix:
    #     for j in i:
    #         if j != 0:
    #             res += j*m.log(j)
    res =  func_5(matrix)+func_2(matrix)
    return res

def func_4(matrix):
    """H(X|Y)"""
    tmp = []
    res = 0
    for i in matrix:
        tmp.append(sum(i))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i,j] != 0:
                res += matrix[i,j]*m.log(tmp[i]/matrix[i,j],2)
    return res

def func_5(matrix):
    """H(Y|X)"""
    tmp = []
    res = 0
    tmp = [sum(x) for x in zip(*matrix)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i, j] != 0:
                res += matrix[i, j] * m.log(tmp[i] / matrix[i, j], 2)
    return res

def func_6(matrix):
    """I(XY)"""
    res = func_1(matrix) - func_4(matrix)
    return res


def main():
    s=read.readtxt('sa')

    # func_5(s)


    result = []
    result.append(func_1(s))
    result.append(func_2(s))
    result.append(func_3(s))
    result.append(func_4(s))
    result.append(func_5(s))
    result.append(func_6(s))

    read.writetxt(result)

if __name__ == "__main__":
    main()


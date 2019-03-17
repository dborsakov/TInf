import numpy as np

def readtxt (name):
    """ Считывает мссив из файла и возвращает в виде матрицы pandas"""
    with open('matrix.txt', 'r') as f:
        l = []
        for line in f:
            line = line.strip()
            if len(line) > 0:
                l.append([int(n) for n in line.split()])
    res = np.array(l)
    return(res)
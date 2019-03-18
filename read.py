import numpy as np

def readtxt (name):
    """ Считывает мссив из файла и возвращает в виде матрицы pandas"""
    with open('matrix.txt', 'r') as f:
        l = []
        for line in f:
            line = line.strip()
            if len(line) > 0:
                l.append([float(n) for n in line.split()])
    res = np.array(l)
    f.close()
    return(res)

def writetxt (result):
    """Записывает результат в файл"""
    t = [' H(X) ', ' H(Y) ', ' H(XY) ', ' H(X|Y) ', ' H(Y|X) ', ' I(XY)\n ']
    f = open("output.txt", "w")
    for i in t:
        f.write(i)
    for i in str(result):
        f.write(i)
    f.close()
    return 0
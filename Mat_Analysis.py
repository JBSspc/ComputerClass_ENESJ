import numpy as np
import sys

class MatAnalysis:

    def addMat(self,mat1,mat2):
        if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
            matR = []
            for i in range(len(mat1)):
                matR.append([])
                for j in range(len(mat1[0])):
                    matR[i].append(mat1[i][j]+mat2[i][j])
            return matR
        else:
            return None

    def subsMat(self,mat1,mat2):
        if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
            matR = []
            for i in range(len(mat1)):
                matR.append([])
                for j in range(len(mat1[0])):
                    matR[i].append(mat1[i][j]-mat2[i][j])
            return matR
        else:
            return None

def main():
    a = [[21,18,35],
         [19,11,21],
         [12,15,20]]
    b = [[11,7,21],
         [9,15,24],
         [23,8,12]]

    maObj = MatAnalysis()
    suma = maObj.addMat(a,b)
    if suma == None:
        print('No se pueden sumar')
    else:
        print('\nSuma:')
        for row in suma:
            print('[', end=' ')
            for element in row:
                print(element, end=' ')
            print(']')

    resta = maObj.subsMat(a,b)
    if resta == None:
        print('No se pueden restar')
    else:
        print('\nResta:')
        for row in resta:
            print('[', end=' ')
            for element in row:
                print(element, end=' ')
            print(']')      

if __name__=='__main__':
    main()

"""
Referencias:
    https://www.youtube.com/watch?v=CDozWggBP6Y
"""
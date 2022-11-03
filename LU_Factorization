import numpy as np
from pprint import pprint

class FactLU:
    def LU_factorization(self, m, matrix,u,l):
        for k in range(0,m):
            for r in range(0,m):
                if(k==r):
                    l[k,r]=1
                if(k<r):
                    factor = (matrix[r,k]/matrix[k,k])
                    l[r,k]=factor
                    for c in range(0,m):
                        matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])
                        u[r,c]=matrix[r,c]
        return l,u

def main():
    print('======= Descomposición LU para matrices cuadradas =======')
    m = int(input('Número de renglones de la matriz: '))
    matrix = np.zeros([m,m])
    u = np.zeros([m,m])
    l = np.zeros([m,m])
    print('Introduce los elementos de la matriz\n')
    for r in range(0,m):
        for c in range(0,m):
            matrix[r,c]=(input('Elemnto a['+str(r)+','+str(c)+']: '))
            matrix[r,c]=float(matrix[r,c])
            u[r,c]=matrix[r,c]
    
    luObj=FactLU()
    L,U= luObj.LU_factorization(m, matrix,u,l)

    print('Impresión de resultados\n')
    print('Matriz L')
    pprint(L)
    print('\nMatriz U')
    pprint(U)

if __name__ =='__main__':
    main()
    
"""
Referencias: 
    cctmexico. (2016). Python: Factorización de matrices LU (Paso a paso, básico). Recuperado el 03 de noviembre de 2021, de sitio web:
            https://www.youtube.com/watch?v=FpVeXhAQg9w&list=PLyVtINljb1ojgJHtqmRooqSiEa70NGyCB&index=12&t=1s

"""


import sys
import numpy as np
from pprint import pprint

"""class Graph:
    def __init__(self):

    def plotLine():"""


class PowerMethod:
    def __init__(self, tol):
        self.tol = tol

    def MaxEigenPowerMethod(self, M, X0, tol, maxIter):
        # Initialize variables
        normX = np.zeros_like(X0)
        lamda0 = 0
        lamda1 = 0
        cont = 0
        
        # Variables to graph error
        error = []
        iters = []
        iter = 0

        error.append(np.inf)

        while(error[iter] > tol or iter < maxIter):
            # Multiplicación de M x X0
            X1 = M @ X0
            #print(X1)
           
            
            # Calcular el valor máximo del vector X1
            lamda1 = np.amax(X1)

            # Normaliza el vector 
            normX1 = X1 / lamda1
            
            error.append(abs(lamda1 - lamda0))
            
            lamda0 = lamda1
            X0 = normX1
            iter+=1

        return lamda1, X0
    
    
    def MinEigenPowerMethod(self, M, X0, tol, maxIter):
        # Initialize variables
        normX = np.zeros_like(X0)
        lamda0 = 0
        lamda1 = 0
        cont = 0
        
        # Variables to graph error
        error = []
        iters = []
        iter = 0

        error.append(np.inf)

        while(error[iter] > tol or iter < maxIter):
            # Multiplicación de M x X0
            X1 = np.linalg. inv(M) @ X0
            #print(X1)
           
            
            # Calcular el valor máximo del vector X1
            lamda1 = np.amax(X1)

            # Normaliza el vector 
            normX1 = X1 / lamda1
            
            error.append(abs(lamda1 - lamda0))
            
            lamda0 = lamda1
            X0 = normX1
            iter+=1

        return lamda1, X0
         

def main():
    n = 3
    #M = np.random.randint(1, 5 ,size =(n, n))

    #M = np.zeros((n,n))
    
    M = np.array([[2,2,1],
        [1,3,1],
        [1,2,2]])
    
    X0 = np.array([1,0,0])
    print('\n======= Método de las potencias =======')
    print('\nMatriz original: ')
    pprint(M)

    tol = 0.0001
    maxIter = 10000

    objP = PowerMethod(tol)
    maxEigenVal, maxEigenVec = objP.MaxEigenPowerMethod(M, X0, tol, maxIter)
    minEigenVal, minEigenVec = objP.MinEigenPowerMethod(M, X0, tol, maxIter)
    
    print("\nEl eigen valor máximo es:", maxEigenVal, " \nSu eigenvecor asociado es:", maxEigenVec)
    print("\nEl eigen valor mínimo es:", minEigenVal, " \nSu eigenvecor asociado es:", minEigenVec)
    


    

    

if __name__ == "__main__":
    main() 
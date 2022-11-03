import numpy as np
from pprint import pprint

class Dec_QR:
    def QR_Decomposition(self,A):
        n, m = A.shape # get the shape of A

        Q = np.empty((n, n)) # initialize matrix Q
        u = np.empty((n, n)) # initialize matrix u

        u[:, 0] = A[:, 0]
        Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])

        for i in range(1, n):

            u[:, i] = A[:, i]
            for j in range(i):
                u[:, i] -= (A[:, i] @ Q[:, j]) * Q[:, j] # get each u vector

            Q[:, i] = u[:, i] / np.linalg.norm(u[:, i]) # compute each e vetor

        R = np.zeros((n, m))
        for i in range(n):
            for j in range(i, m):
                R[i, j] = A[:, j] @ Q[:, i]

        return Q, R

    def diag_sign(self,A):
        "Compute the signs of the diagonal of matrix A"

        D = np.diag(np.sign(np.diag(A)))

        return D

    def adjust_sign(self,Q, R):
        """
        Adjust the signs of the columns in Q and rows in R to
        impose positive diagonal of Q
        """

        D = self.diag_sign(Q)

        Q[:, :] = Q @ D
        R[:, :] = D @ R

        return Q, R    

def main():
    A = np.array([[1.0, 1.0, 0.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0]])
    qrObj=Dec_QR()
    Q, R = qrObj.adjust_sign(*qrObj.QR_Decomposition(A))

    print("\nMatriz A:")
    pprint(A)
    print("\nMatriz Q:")
    pprint(Q)
    print("\nMatriz R:")
    pprint(R)

if __name__=='__main__':
    main()


"""
Referencias:
    https://python.quantecon.org/qr_decomp.html
"""
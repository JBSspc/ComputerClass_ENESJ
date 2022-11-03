from math import sqrt
from pprint import pprint
#from itertools import imap

class qrFact:

    def cmp(self, a,b):
        return (a>b)-(a<b)

    def multMat(self, M,N):
        tuple_N = zip(*N)
        return [[sum(el_m*el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

    def matTranspose(self, M):
        n=len(M)
        return [[M[i][j] for i in range(n)] for j in range(n)]

    def norm(self, x):
        return sqrt(sum([x_1**2 for x_1 in x]))

    def Q_i(self,Q_min, i, j, k):
        if i < k or j < k:
            return float(i==j)
        else:
            return Q_min[i-k][j-k]

    def houseHolderReflect(self, A):
        n = len(A)
        R = A
        Q = [[0.0]*n for i in range(n)]

        for k in range(n-1):
            I = [[float(i==j) for i in range(n)] for j in range(n)]

            x = [row[k] for row in R[k:]]
            e = [row[k] for row in I[k:]]
            alpha = -self.cmp(x[0],0)* self.norm(x)

            u = list(map(int, lambda p,q: p + alpha * q, x, e))
            norm_u = self.norm(u)
            v = list(map(int, lambda p: p/norm_u,u))

            Q_min = [[float(i==j) - 2.0 * v[i]*v[j] for i in range(n-k)] for j in range(n-k)]

            Q_t = [[self.Q_i(Q_min,i,j,k) for i in range(n)] for j in range(n)]

            if k == 0:
                Q = Q_t
                R = self.multMat(Q_t,A)
            else:
                Q = self.multMat(Q_t,Q)
                R = self.multMat(Q_t,R)

        return self.matTranspose(Q), R

def main():

    A = [[12, -51, 4], [6, 167, -68], [-4, 24, -41]]
    qrObj = qrFact()
    Q,R = qrObj.houseHolderReflect(A)

    print("A:")
    pprint(A)

    print("Q:")
    pprint(Q)

    print("R:")
    pprint(R)

if __name__=='__main__':
    main()

"""
Referencias:
    https://www.quantstart.com/articles/QR-Decomposition-with-Python-and-NumPy/
"""
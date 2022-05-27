import re
from sympy import im


import numpy as np
import sys
import matplotlib.pyplot  as plt

class EquationSolver:

    # def __init__(self):
        # self.equation = equations
            # pass
    def LUdecomposition(self,a, n):
        L = np.zeros((n, n))
        U = np.zeros((n, n))
        x = np.zeros(shape=(n, 1))

        for i in range(n):
            for j in range(n):
                U[i][j] = a[i][j]  #U is the same as a but without answers (a --> augmented matrix,  U --> not augmented)
                if i == j:
                    L[i][j] = 1  #diagonals = 1
                else:
                    L[i][j] = 0

        # Forward Elimination
        for i in range(n):
            if U[i][i] == 0.0:
                # root_label.config(text="Division by zero")
                # root_label.grid(row=2, column=5)
                raise ValueError('Division by zero')
                return None

            for j in range(i + 1, n):
                ratio = U[j][i] / U[i][i]
                L[j][i] = ratio  #lower triangular matrix containing ratios

                for k in range(n):  #eliminate (to construct an upper triangular matrix)
                    U[j][k] = U[j][k] - ratio * U[i][k]

        # Forward Substitution  (L * y = b)
        y = np.zeros(n)
        y[0] = a[0][n]  #answer in the augmented matrix

        for i in range(1, n):
            y[i] = a[i][n]  #results

            for j in range(i):
                y[i] = y[i] - L[i][j] * y[j]  #There is no coeff. division as diagonals = 1 in L

        # Back Substitution (U * x = y)
        x[n - 1] = y[n - 1] / U[n - 1][n - 1]

        for i in range(n - 2, -1, -1):
            x[i] = y[i]  #results

            for j in range(i + 1, n):
                x[i] = x[i] - U[i][j] * x[j]

            x[i] = x[i] / U[i][i]
        return x



# a: augmented matrix
# n: number of equations

    def Gauss_jordan(self,a, n , Ea = 0.001):
            errdigits = 0
            while Ea < 1:
                Ea = Ea * 10
                errdigits += 1
            x = np.zeros(n)
            # Applying Gauss Jordan Elimination
            for i in range(n):
                if a[i][i] == 0.0:
                    # sys.exit('Cannot use Gausses Jordan method Divide by zero detected!')
                    raise ValueError('Division by zero')
                if a[i][i] != 1:
                    y = a[i][i]
                    for z in range(n + 1):
                        a[i][z] = a[i][z] / y

                for j in range(n):
                    if i != j:
                        rat = a[j][i]
                        for k in range(n + 1):
                            a[j][k] = a[j][k] - rat * a[i][k]

            # Obtaining Solution
            for k in range(n):
                if a[k][k] == 0:
                    if a[k][n] == 0:
                        # sys.exit('Infinite number of solutions')
                        raise ValueError('Infinite number of solutions')
                    else:
                        raise ValueError('No solution')
                        # sys.exit('No solution')
            # print(a)
            for i in range(n):
                x[i] = a[i][n]
                # print(x[i])
            self.write_output(x)

            # print('x = ',x)

            return x
        

    def write_output(self,x):
        f = open("demofile3.txt", "w")
        f.write(" The roots are:\n")
        for i in range(len(x)):
            f.write(str(x[i]))
            f.write(" ")
        f.close()

    def lu_decomp(self,a, n):

        L = np.zeros((n, n))
        U = np.zeros((n, n))
        x = np.zeros(shape=(n, 1))

        for i in range(n):
            for j in range(n):
                U[i][j] = a[i][j]  # U is the same as a but without answers (a --> augmented matrix,  U --> not augmented)
                if i == j:
                    L[i][j] = 1  # diagonals = 1
                else:
                    L[i][j] = 0

        # Forward Elimination
        for i in range(n):
            if U[i][i] == 0.0:
                # root_label.config(text="Division by zero")
                # root_label.grid(row=2, column=5)
                raise ValueError('Division by zero')
                # return None
            for j in range(i + 1, n):
                ratio = U[j][i] / U[i][i]
                L[j][i] = ratio  # lower triangular matrix containing ratios
                for k in range(n):  # eliminate (to construct an upper triangular matrix)
                    U[j][k] = U[j][k] - ratio * U[i][k]

        # Forward Substitution  (L * y = b)
        y = np.zeros(n)
        y[0] = a[0][n]  # answer in the augmented matrix
        for i in range(1, n):
            y[i] = a[i][n]  # results
            for j in range(i):
                y[i] = y[i] - L[i][j] * y[j]  # There is no coeff. division as diagonals = 1 in L

        # Back Substitution (U * x = y)
        x[n - 1] = y[n - 1] / U[n - 1][n - 1]
        for i in range(n - 2, -1, -1):
            x[i] = y[i]  # results
            for j in range(i + 1, n):
                x[i] = x[i] - U[i][j] * x[j]
            x[i] = x[i] / U[i][i]

        print('x = ',x)
        return x

        

    def gauss_elimination(self , a,b,n):
        # n = 3
        # a = np.array([[3, 2, 1], [2, 3, 0], [0, 0, 2]], float)
        # b = np.array([6, 7, 4], float)
        x = np.zeros(n, float)

        for k in range(n - 1):
            for i in range(k + 1, n):
                if abs(a[i, k]) > abs(a[k, k]):
                    a[[k, i]] = a[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break

            # applies the elimination below the fixed row
            for i in range(k + 1, n):
                if a[i, k] == 0:
                    continue
                factor = a[k, k] / a[i, k]
                for j in range(k, n):
                    a[i, j] = a[k, j] - a[i, j] * factor  # we also calculate the b vector of each row
                b[i] = b[k] - b[i] * factor

        x[n - 1] = b[n - 1] / a[n - 1, n - 1]
        for i in range(n - 2, -1, -1):
            sum_ax = 0
            for j in range(i + 1, n):
                sum_ax += a[i, j] * x[j]
            x[i] = (b[i] - sum_ax) / a[i, i]

        print(f"x = {x}")
        return x

    def gauss_seidal(self,A, b,x, tolerance, max_iterations):
        #x is the initial condition
        iter1 = 0
        iter_ar = []
        x_ar = []

        for i in range(A.shape[0]):
            temp = []
            x_ar.append(temp)

        #Iterate
        for k in range(max_iterations):
            iter_ar.append(iter1)
            for i in range(A.shape[0]):
                
                x_ar[i].append(x[i]) 
            # x_ar.append(x)
            iter1 = iter1 + 1
            print ("The solution vector in iteration", iter1, "is:", x)    
            x_old  = x.copy()
            
            #Loop over rows
            for i in range(A.shape[0]):
                x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]

            #Stop condition 
            #LnormInf corresponds to the absolute value of the greatest element of the vector.
            
            LnormInf = max(abs((x - x_old)))/max(abs(x_old))   
            print ("The L infinity norm in iteration", iter1,"is:", LnormInf)
            if  LnormInf < tolerance:
                break

        plt.figure()
        labels = []
        print(len(x_ar))
        print(len(iter_ar))
        for i in range(len(x_ar)):
            plt.plot(iter_ar, x_ar[i])
            labels.append('x' + str(i))

        plt.xlabel('Iterations')
        plt.ylabel('x')
        plt.legend(labels)
        plt.show()
            
        return x,iter1
   
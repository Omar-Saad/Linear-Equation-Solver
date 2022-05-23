from sympy import im


import numpy as np
import sys

class EquationSolver:

    def __init__(self, equations):
        self.equation = equations


    def lu_decomp(a, b, n, x, tol, er):
        s = np.zeros(shape=(n, 1))
        o = np.zeros(shape=(n, 1))

        er = 0

        for i in range(n):
            o[i] = i
            s[i] = abs(a[i][1])
            for j in range(2, n):
                if abs(a[i][j]) > s[i]:
                    s[i] = abs(a[i][j])

        for k in range(n - 1):
            p = k
            big = abs(a[o[k]][k] / s[o[k]])
            for i in range(k + 1, n):
                dummy = abs(a[o[i]][k] / s[o[i]])
                if dummy > big:
                    big = dummy
                    p = i
            dummy = o[p]
            o[p] = o[k]
            o[k] = dummy

            if (abs(a[o[k]][k]) / s[o[k]]) < tol:
                er = -1
                return
            for i in range(k + 1, n):
                factor = a[o[i]][k] / a[o[k]][k]
                a[o[i]][k] = factor
                for j in range(k + 1, n):
                    a[o[i]][j] = a[o[i]][j] - factor * a[o[k]][j]

        if (abs(a[o[n]][n]) / s[o[n]]) < tol:
            er = -1

        if er != -1:
            y = np.zeros(shape=(n, 1))
            y[o[1]] = b[o[1]]
            for i in range(2, n):
                sum = b[o[i]]
                for j in range(i - 1):
                    sum -= a[o[i]][j] * y[o[j]]
                y[o[i]] = sum
            x[n] = y[o[n]] / a[o[n]][n]
            for i in range(n - 1, 1, -1):
                sum = 0
                for j in range(i + 1, n):
                    sum += a[o[i]][j] * x[j]
                x[i] = (y[o[i]] - sum) / a[o[i]][i]
                
    
    def gaussElimination(self):
        n = int(input('Enter number of unknowns: '))
        # Augmented matrix (numpy array of n x n+1 size)
        augment = np.zeros((n, n + 1))
        # Solution vector
        x = np.zeros(n)
        # Reading augmented matrix coefficients
        print('Enter Augmented Matrix Coefficients:')
        for i in range(n):
            for j in range(n + 1):
                augment[i][j] = float(input(f"a[{str(i)}][{str(j)}] = "))

        # Applying Gauss Elimination
        for i in range(n):
            if augment[i][i] == 0.0:
                sys.exit('Error: Division by zero')
            for j in range(i + 1, n):
                ratio = augment[j][i] / augment[i][i]
                for k in range(n + 1):
                    augment[j][k] = augment[j][k] - ratio * augment[i][k]

        # Back Substitution
        x[n - 1] = augment[n - 1][n] / augment[n - 1][n - 1]
        for i in range(n - 2, -1, -1):
            x[i] = augment[i][n]
            for j in range(i + 1, n):
                x[i] = x[i] - augment[i][j] * x[j]
            x[i] = x[i] / augment[i][i]

        # Displaying solution
        print('\nSolution:')
        for i in range(n):
            print('X_%d = %0.2f' % (i, x[i]), end='\t')

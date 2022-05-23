import sys
import numpy as np

if __name__ == '__main__':
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

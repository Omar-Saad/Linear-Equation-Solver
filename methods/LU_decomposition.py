# import numpy




# def lu_decomp(a, b, n, x, tol, er):
#     s = numpy.zeros(shape=(n, 1))
#     o = numpy.zeros(shape=(n, 1))

#     er = 0

#     for i in range(n):
#         o[i] = i
#         s[i] = abs(a[i][1])
#         for j in range(2, n):
#             if abs(a[i][j]) > s[i]:
#                 s[i] = abs(a[i][j])

#     for k in range(n - 1):
#         p = k
#         big = abs(a[o[k]][k] / s[o[k]])
#         for i in range(k + 1, n):
#             dummy = abs(a[o[i]][k] / s[o[i]])
#             if dummy > big:
#                 big = dummy
#                 p = i
#         dummy = o[p]
#         o[p] = o[k]
#         o[k] = dummy

#         if (abs(a[o[k]][k]) / s[o[k]]) < tol:
#             er = -1
#             return
#         for i in range(k + 1, n):
#             factor = a[o[i]][k] / a[o[k]][k]
#             a[o[i]][k] = factor
#             for j in range(k + 1, n):
#                 a[o[i]][j] = a[o[i]][j] - factor * a[o[k]][j]

#     if (abs(a[o[n]][n]) / s[o[n]]) < tol:
#         er = -1

#     if er != -1:
#         y = numpy.zeros(shape=(n, 1))
#         y[o[1]] = b[o[1]]
#         for i in range(2, n):
#             sum = b[o[i]]
#             for j in range(i - 1):
#                 sum -= a[o[i]][j] * y[o[j]]
#             y[o[i]] = sum
#         x[n] = y[o[n]] / a[o[n]][n]
#         for i in range(n - 1, 1, -1):
#             sum = 0
#             for j in range(i + 1, n):
#                 sum += a[o[i]][j] * x[j]
#             x[i] = (y[o[i]] - sum) / a[o[i]][i]

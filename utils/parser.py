import numpy
from sympy import *


class EquationParser:
    def __init__(self, file_path):
        self.method_name = None
        self.num_of_equations = None
        self.A = None
        self.B = None
        self.variables = None


    def readFunctionFromFile(self,fileName):
        input_file = open(fileName, "r")
        lines = input_file.readlines()
        input_file.close()
        num_of_equations = int(lines[0])
        method_name = lines[1]

        variables = set()
        for line in lines[2:2 + num_of_equations]:
            for c in line:
                if c.isalpha():
                    variables.add(c)


        variables = list(variables)
        variables.sort()
        n = len(variables)

        # print(num_of_equations)
        # print(method_name)
        # print(variables)

        # A*X = B

        A = numpy.zeros(shape=(n, n))
        B = numpy.zeros(shape=(n, 1))
        equations = '\n'.join(lines[2: 2 + num_of_equations]).replace(" ", "").replace("*", "")
        #     a          x  
        #    n*n        x*1       n*1   
        # [1 2 3 ] * [x y z] = [0 2 3]

        for i, line in enumerate(lines[2: 2 + num_of_equations]):
            expr = sympify(line)

            for j, c in enumerate(variables):
                A[i, j] = expr.coeff(c)
            
            
            expr = Poly(expr, symbols(", ".join(variables)))
            nums = expr.coeffs()

            B[i] = -1 * nums.pop()
        
        self.init_values = None

        if "seidel" in method_name.lower():
            init_values = numpy.asarray(list(map(float, lines[-1].split())))
            self.init_values = init_values

            # return method_name , num_of_equations, A, B, variables, init_values  
        
        self.method_name = method_name
        self.num_of_equations = num_of_equations
        self.A = A
        self.B = B
        self.variables = variables

        

        # return method_name , num_of_equations, A, B, variables


if __name__ == "__main__":
    filename = input("Enter name of input file: ")
    fp = EquationParser(filename)
    fp.readFunctionFromFile(filename)
    print(fp.method_name)
    print(fp.num_of_equations)
    print(fp.A)
    print(fp.B)
    print(fp.variables)



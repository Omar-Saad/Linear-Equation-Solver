import tkinter as tk
from tkinter import ttk
from tkinter import font
from unittest import result
import numpy as np
import matplotlib as plt
from tkinter import messagebox
from tkinter import OptionMenu
from tkinter import Toplevel
import constants
from methods.equation_solver import EquationSolver
from screens.results_screen import ResultsScreen
from utils.parser import EquationParser
import time


class EquationEntryScreen(Toplevel):
    def __init__(self, master, metodName, numOfEquations):
        super().__init__(master=master)

        self.title("Linear Equations Solver")
        self.numOfEquations = numOfEquations
        self.methodName = metodName
        # self.iconbitmap("res/logo.ico")

        self.window_width = 750
        self.window_height = 200 + numOfEquations * 50

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - self.window_width / 2)
        center_y = int(screen_height / 2 - self.window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f"{self.window_width}x{self.window_height}+{center_x}+{center_y}")

        FONT = "Verdana"
        largeFont = (FONT, 20)
        mediumFont = (FONT, 16)
        smallFont = (FONT, 14)

        welcomeLabel = ttk.Label(
            self,
            text="Equation Entry for {} method".format(self.methodName),
            font=largeFont,
        )

        # command = lambda : self.plot_function())

        # welcomeLabel.pack()
        welcomeLabel.grid(
            row=0, column=0, padx=8, pady=8, sticky="W", columnspan=2, rowspan=1
        )
        self.functions_entry = []

        for i in range(numOfEquations):
            funLabel = ttk.Label(
                self, text="Function {}".format(i + 1), font=mediumFont
            )
            funEntry = ttk.Entry(self, width=20, font=smallFont)

            self.functions_entry.append(funEntry)

            funLabel.grid(row=i + 1, column=0, padx=10, pady=10)
            funEntry.grid(row=i + 1, column=1, padx=10, pady=10)

        iterationsLabel = ttk.Label(self, text="Number of Iterations", font=mediumFont)
        iterationsEntry = ttk.Entry(self, width=20, font=smallFont)
        iterationsEntry.insert(0, "50")
        self.iterationsEntry = iterationsEntry

        epsilonLabel = ttk.Label(self, text="Default Epsilon", font=mediumFont)
        epsilonEntry = ttk.Entry(self, width=20, font=smallFont)
        epsilonEntry.insert(0, "0.00001")
        self.epsilonEntry = epsilonEntry

        iterationsLabel.grid(row=numOfEquations + 2, column=0, padx=10, pady=10)
        iterationsEntry.grid(row=numOfEquations + 2, column=1, padx=10, pady=10)

        epsilonLabel.grid(row=numOfEquations + 3, column=0, padx=10, pady=10)
        epsilonEntry.grid(row=numOfEquations + 3, column=1, padx=10, pady=10)

        button = ttk.Button(self, text="Solve Equations")
        button.bind("<Button>", lambda e: self.goButtonCallback())

        if self.methodName == constants.METHODS_NAME[3]:
            # TODO : Arguments name
            arg1Label = ttk.Label(self, text="x1", font=mediumFont)
            arg1Entry = ttk.Entry(self, width=5, font=smallFont)
            self.arg1Entry = arg1Entry

            arg2Label = ttk.Label(self, text="x2", font=mediumFont)
            arg2Entry = ttk.Entry(self, width=5, font=smallFont)
            self.arg2Entry = arg2Entry

            arg3Label = ttk.Label(self, text="x2", font=mediumFont)
            arg3Entry = ttk.Entry(self, width=5, font=smallFont)
            self.arg3Entry = arg3Entry

            arg1Label.grid(row=numOfEquations + 3, column=0, padx=10, pady=10)
            arg2Label.grid(row=numOfEquations + 3, column=1, padx=10, pady=10)
            arg3Label.grid(row=numOfEquations + 3, column=2, padx=10, pady=10)

        button.grid(row=numOfEquations + 4, column=1, padx=10, pady=10)

    def getEpsilon(self):
        try:
            return float(self.epsilonEntry.get())
        except ValueError:
            messagebox.showerror("Error", "Epsilon must be a number")
            return None

    def getMethodName(self):
        return self.methodName

    def getNumberOfIetrations(self):
        try:
            num = int(self.iterationsEntry.get())
            if num > 0:
                return num
            else:
                messagebox.showerror("Error", "Number of iterations must be positive")
                return None
        except:
            messagebox.showerror("Error", "Number of Ietrations Must be an integer")
            return None

    def getFunctions(self):
        functions = []
        for i in range(self.numOfEquations):
            functions.append(self.functions_entry[i].get())
        return functions

    def goButtonCallback(self):

        # TODO : Check if all the entries are valid
        # TODO : Call the method functions and return the result
        for fun in self.functions_entry:
            if fun.get() == "":
                messagebox.showerror("Error", "All the entries must be filled")
                return
        try:
            A,B,varaibles = EquationParser().parseFunctions(self.getFunctions())
        except:
            messagebox.showerror("Error", "Invalid Equation")
            return
        
        results = []

        if self.methodName == constants.METHODS_NAME[0]:
            # Gaussian-elimination
            # TODO
            solver = EquationSolver()
            
            start_time = time.time()
            results = solver.gaussElimination(np.concatenate((A, B), axis=1), len(varaibles))
            results+=[self.getNumberOfIetrations(),time.time() - start_time]


        if self.methodName == constants.METHODS_NAME[1]:
            # LU decomposition
            # TODO
            solver = EquationSolver()
            
            start_time = time.time()
            results = solver.LUdecomposition(np.concatenate((A, B), axis=1), len(varaibles))
            results+=[self.getNumberOfIetrations(),time.time() - start_time]

        
        if self.methodName == constants.METHODS_NAME[2]:
            # Gaussian-Jordan
            # TODO
            solver = EquationSolver()
      
            
            start_time = time.time()
            results = solver.LUdecomposition(np.concatenate((A, B), axis=1), len(varaibles))
            results+=[self.getNumberOfIetrations(),time.time() - start_time]


        if self.methodName == constants.METHODS_NAME[3]:
            # Gauss-Seidel
            # TODO
            solver = EquationSolver()
         
            start_time = time.time()
            results = solver.LUdecomposition(np.concatenate((A, B), axis=1), len(varaibles))
            results+=[self.getNumberOfIetrations(),time.time() - start_time]


        

        return ResultsScreen(self, self.getMethodName(), self.numOfEquations , varaibles , results)

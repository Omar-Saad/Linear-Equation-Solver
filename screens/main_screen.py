# # import sys
# # sys.path.append(".")
# import os, sys

# p = os.path.abspath('.')
# sys.path.insert(1, p)


from utils.parser import EquationParser
import tkinter as tk
from tkinter import ttk
from tkinter import font
import numpy as np
import matplotlib as plt
from tkinter import messagebox
from tkinter import OptionMenu
from tkinter import Toplevel
from methods.equation_solver import EquationSolver
import time


from screens.equation_entry_screen import EquationEntryScreen

import constants
from screens.results_screen import ResultsScreen
from tkinter import filedialog



# Main Gui Screen for the application

class MainScreen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Linear Equations Solver")
        # self.iconbitmap("res/logo.ico")
        
            
        self.window_width = 750
        self.window_height = 350

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - self.window_width / 2)
        center_y = int(screen_height/2 - self.window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')

        FONT = "Verdana"
        largeFont = (FONT, 20)
        mediumFont = (FONT,16 )
        smallFont = (FONT, 14)
        

        welcomeLabel = ttk.Label(self, text="Welcome To Equation Solver", font=largeFont)
        methodLabel = ttk.Label(self, text="Method Name", font=mediumFont)

        
        # datatype of menu text
        self.clicked = tk.StringVar()
        
        # initial menu text
        self.clicked.set( "Gaussian-elimination" )
        
        # Create Label
        self.label = tk.Label( self , text = " " )
        # self.label.pack()

        drop = OptionMenu(self , self.clicked , *constants.METHODS_NAME )
        # drop.pack()

        numberOfEquationsLabel = ttk.Label(self, text="Number of Equations", font=mediumFont)
        self.numberOfEquationsEntry = ttk.Entry(self, width=20,font = smallFont)
   
       



        button = ttk.Button(self, text ="Go to Enter Equtions")
        # ,command = lambda : self.show())
        button.bind("<Button>",lambda e:self.goButtonCallback())

        solveFilebutton = ttk.Button(self, text ="Input Equations from File")
        # ,command = lambda : self.show())
        solveFilebutton.bind("<Button>",lambda e:self.solveFromFileButtonCallback())
 
# btn.pack(pady = 10)
          
        # welcomeLabel.pack()
        welcomeLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

        methodLabel.grid(row = 1, column = 0, padx = 10, pady = 10 )
        drop.grid(row = 1, column = 1, padx = 10, pady = 10)

        numberOfEquationsLabel.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.numberOfEquationsEntry.grid(row = 2, column = 1, padx = 10, pady = 10)

   
        button.grid(row = 3, column = 1, padx =10, pady = 10 , columnspan=1)

        solveFilebutton.grid(row = 4, column = 1, padx = 10, pady = 10,columnspan=1)
   
   
    def goButtonCallback(self):
    
         return EquationEntryScreen(self , self.getMethodName() , self.getNumberOfEquations())


    def solveFromFileButtonCallback(self):
        file_path = filedialog.askopenfilename()
        parser = EquationParser()
        parser.readFunctionFromFile(file_path)
        A = parser.A
        B = parser.B
        variables = parser.variables
        results = []

        # print('name = ',parser.method_name)
        try:
            if parser.method_name == constants.METHODS_NAME[0]:
                # Gaussian-elimination
                # TODO
                solver = EquationSolver()
                
                start_time = time.time()
                results = solver.gauss_elimination(A,B, len(variables))
                results = np.append(results , [0,time.time() - start_time], axis=0)


            if parser.method_name == constants.METHODS_NAME[1]:
                # LU decomposition
                # TODO
                solver = EquationSolver()
                
                start_time = time.time()
                results = solver.lu_decomp(np.concatenate((A, B), axis=1), len(variables))
                print('resulst = ',results)
                # reshape into 1d
                results = np.reshape(results,(len(results),))
                
                results = np.append(results , [0,time.time() - start_time], axis=0)
                print('resulst 2= ',results)

                
            if parser.method_name == constants.METHODS_NAME[2]:
                # Gaussian-Jordan
                # TODO
                
                solver = EquationSolver()
        
                start_time = time.time()
                results = solver.Gauss_jordan(np.concatenate((A, B), axis=1), len(variables))
                print('resulst = ',results)
                results = np.append(results , [0,time.time() - start_time], axis=0)
                print('resulst 2= ',results)

            if parser.method_name == constants.METHODS_NAME[3]:
                # Gauss-Seidel
                # TODO
                print('aa')
                solver = EquationSolver()
                # print(parser.init_values)
                x = parser.init_values

                start_time = time.time()
                results,iterations = solver.gauss_seidal(A,B,x  , 0.00001 ,  50)
            
                results = np.append(results , [iterations,time.time() - start_time], axis=0)
            
        except:
            messagebox.showerror("Error", "Error in solving the equation")
            return


    
        return ResultsScreen(self , parser.method_name.strip() , int(parser.num_of_equations), parser.variables , results=results) 

    def getMethodName(self):
        return self.clicked.get()
    
    def getNumberOfEquations(self):
        try :
            return int(self.numberOfEquationsEntry.get())
        except:
            messagebox.showerror("Error","Number of Equations Must be a number")
            return None
        # return self.numberOfEquationsEntry.get()
    

    def show(self):
        self.label.config( text = self.clicked.get() )
  




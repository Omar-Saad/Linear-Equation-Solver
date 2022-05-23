# # import sys
# # sys.path.append(".")
# import os, sys

# p = os.path.abspath('.')
# sys.path.insert(1, p)


import tkinter as tk
from tkinter import ttk
from tkinter import font
import numpy as np
import matplotlib as plt
from tkinter import messagebox
from tkinter import OptionMenu
from tkinter import Toplevel


from screens.equation_entry_screen import EquationEntryScreen

import constants


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
 
# btn.pack(pady = 10)
          
        # welcomeLabel.pack()
        welcomeLabel.grid(row = 0, column = 1, padx = 10, pady = 10)

        methodLabel.grid(row = 1, column = 0, padx = 10, pady = 10 )
        drop.grid(row = 1, column = 1, padx = 10, pady = 10)

        numberOfEquationsLabel.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.numberOfEquationsEntry.grid(row = 2, column = 1, padx = 10, pady = 10)

   
        button.grid(row = 3, column = 1, padx = 10, pady = 10)
   
   
    def goButtonCallback(self):
         if self.getNumberOfEquations() == "":
            messagebox.showerror("Error","Please enter the number of equations")
            return

         if not self.getNumberOfEquations().isdigit():
            messagebox.showerror("Error","Number of Equations Must be a number")
            return


        
         return EquationEntryScreen(self , self.getMethodName())

    def getMethodName(self):
        return self.clicked.get()
    
    def getNumberOfEquations(self):
        return self.numberOfEquationsEntry.get()
    

    def show(self):
        self.label.config( text = self.clicked.get() )
  

    def replace_operations_from_string(self,func):

        func = func.replace(" ","").lower()
        
        op = {
            'sin':'np.sin',
            'cos':'np.cos',
            'tan':'np.tan',
            'log':'np.log',
            'exp':'np.exp',
            'sqrt':'np.sqrt',
            '^':'**',
            'ln':'np.log',
            'pi':'np.pi',
            }
        for i in op:
            func = func.replace(i,op[i])

        return func

    







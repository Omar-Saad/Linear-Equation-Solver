
import tkinter as tk
from tkinter import ttk
from tkinter import font
import numpy as np
import matplotlib as plt
from tkinter import messagebox
from tkinter import OptionMenu
from tkinter import Toplevel
import constants

class EquationEntryScreen(Toplevel):

 def __init__(self,master,metodName,numOfEquations=3):
        super().__init__(master =master )

        self.title("Linear Equations Solver")
        self.numOfEquations = numOfEquations
        self.methodName = metodName
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
        mediumFont = (FONT,16)
        smallFont = (FONT, 14)
        

        welcomeLabel = ttk.Label(self, text="Equation Entry", font=largeFont)
        

        
       

        button = ttk.Button(self, text ="Solve Equations")
        # command = lambda : self.plot_function())
          
        # welcomeLabel.pack()
        welcomeLabel.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.functions_entry = []


        for i in range(numOfEquations):
            funLabel = ttk.Label(self, text="Function {}".format(i), font=mediumFont)
            funEntry = ttk.Entry(self, width=20,font = smallFont)
            
            self.functions_entry.append(funEntry)

            funLabel.grid(row = i+1, column = 0, padx = 10, pady = 10 )
            funEntry.grid(row = i+1, column = 1, padx = 10, pady = 10)

            
        iterationsLabel = ttk.Label(self, text="Number of Iterations", font=mediumFont)
        iterationsEntry = ttk.Entry(self, width=20,font = smallFont)
        self.iterationsEntry = iterationsEntry

        iterationsLabel.grid(row = numOfEquations+2, column = 0, padx = 10, pady = 10)
        iterationsEntry.grid(row = numOfEquations+2, column = 1, padx = 10, pady = 10)

        if self.methodName == constants.METHODS_NAME[3]:
            # TODO : Arguments name
            arg1Label = ttk.Label(self, text="x1", font=mediumFont)
            arg1Entry = ttk.Entry(self, width=5,font = smallFont)
            self.arg1Entry = arg1Entry
            
            arg2Label = ttk.Label(self, text="x2", font=mediumFont)
            arg2Entry = ttk.Entry(self, width=5,font = smallFont)
            self.arg2Entry = arg2Entry

            arg3Label = ttk.Label(self, text="x2", font=mediumFont)
            arg3Entry = ttk.Entry(self, width=5,font = smallFont)
            self.arg3Entry = arg3Entry

            arg1Label.grid(row = numOfEquations+3, column = 0, padx = 10, pady = 10)
            arg2Label.grid(row = numOfEquations+3, column = 1, padx = 10, pady = 10)
            arg3Label.grid(row = numOfEquations+3, column = 2, padx = 10, pady = 10)


        button.grid(row = numOfEquations+1, column = 1, padx = 10, pady = 10)
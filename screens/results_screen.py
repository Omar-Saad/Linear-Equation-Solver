
import tkinter as tk
from tkinter import ttk
from tkinter import font
import numpy as np
import matplotlib as plt
from tkinter import messagebox
from tkinter import OptionMenu
from tkinter import Toplevel
import constants

class ResultsScreen(Toplevel):

    # resuls : is an array consists of var. results and number of iterations and execution time
    def __init__(self,master,metodName,numOfEquations,variables,results ):
        super().__init__(master =master )

        self.title("Linear Equations Solver")
        self.numOfEquations = numOfEquations
        self.methodName = metodName
        self.result = results
        # self.iconbitmap("res/logo.ico")
        
            
        self.window_width = 750
        self.window_height = 200 + len(results) * 50

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
        

        welcomeLabel = ttk.Label(self, text="Results with {} method".format(self.methodName), font=largeFont)
        welcomeLabel.grid(row = 0, column = 0, padx = 8, pady = 8,sticky='W',columnspan=2,rowspan=1)

        for i in range(numOfEquations):
            rootLabel = ttk.Label(self, text="{} : {}".format(variables[i] , results[i]), font=largeFont)
            
            rootLabel.grid(row = i+1, column = 0, padx = 8, pady = 8,sticky='W',columnspan=2,rowspan=1)

        
        numIetrationsLabel = ttk.Label(self, text="Number of Ietrations : {}".format(results[numOfEquations]), font=largeFont)
            
        numIetrationsLabel.grid(row = numOfEquations+1, column = 0, padx = 8, pady = 8,sticky='W',columnspan=2,rowspan=1)

        executionTimeLabel = ttk.Label(self, text="Execution Time : {}".format(results[-1]), font=largeFont)
            
        executionTimeLabel.grid(row = numOfEquations+2, column = 0, padx = 8, pady = 8,sticky='W',columnspan=2,rowspan=1)

        # welcomeLabel.pack()
        


        

     
  

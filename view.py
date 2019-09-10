#this should make mencoder easy

import os
from menconstruct import MenConstruct
import subprocess
from pathlib import Path
import tkinter as tk

import controller
from configurations import *

class View():

    #Todo
    #pull in a few configurations
    raw_vhs_filepath = RAW_VHS_FILEPATH
    finished_vhs_filepath = FINISHED_VHS_FILEPATH

    screen_geometry = SCREEN_GEOMETRY



    def __init__(self, parent, controller):
        #Wtf is the parent here?
        self.controller = controller
        self.parent = parent
        self.parent.geometry(str(SCREEN_GEOMETRY))
        #self.creat_chess_base()
        self.createInterfaceBase()

        # how to implement frame switch
        # parent.frames = {}
        # self.createFrames(parent)
        # parent.showFrame(StartPage)

        #self.canvas.bind("")

    #Initializer Function
    def createInterfaceBase(self):
        #create layout
        self.createTopMenu()
        self.frameButtonPane = tk.Frame(self.parent, width=200, bg="green")

        self.frameRandom = tk.Frame(self.parent, width = 120, bg="red", relief=tk.SUNKEN)
        self.createButtonPane(self.frameButtonPane)

        self.frameButtonPane.pack(side=tk.LEFT, fill=tk.X, expand=1)
        self.frameRandom.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    #Initializer Function
    def createTopMenu(self):
        #layout for file, edit, help bar
        self.menuBar = tk.Menu(self.parent)
        self.createFileMenu()

    #Initializer Function
    def createFileMenu(self):
        self.fileMenu = tk.Menu(self.menuBar)
        self.fileMenu.add_command(label="New")
        self.fileMenu.add_command(label="Open...")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exitProgram)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.parent.config(menu=self.menuBar)

    #Initializer Function
    def createButtonPane(self, container):
        #create Buttons first
        self.recordButton = tk.Button(container, text="Record", command=self.functionRecord)
        self.convertButton = tk.Button(container, text="Convert", command=self.functionConvert)
        self.playButton = tk.Button(container, text="Play", command=self.functionPlay)
        self.test1Button = tk.Button(container, text="Test1", command=self.functionTest1)
        self.test2Button = tk.Button(container, text="Test2", command=self.functionTest2)
        self.exitButton = tk.Button(container, text="Exit", command=self.exitProgram)

        #Pack your bags
        self.recordButton.pack(fill=tk.X, expand=1)
        self.convertButton.pack(fill=tk.X, expand=1)
        self.playButton.pack(fill=tk.X, expand=1)
        self.test1Button.pack(fill=tk.X, expand=1)
        self.test2Button.pack(fill=tk.X, expand=1)
        self.exitButton.pack(fill=tk.X, expand=1)

    #Initialize Frames
    def createFrames(parent):
        for F in (StartPage, SecondPage):
            frame = F(parent, self)
            self.frames[F] = frame
            frame.pack()
        # self.frames = StartPage(self.frameRandom, self)
        # self.frames = SecondPage(self.frameRandom, self)

    #variable Frames
    def showFrame(parent, cont):
        #looking at the frames list at position cont
        for gone in parent.frames:
            gone.grid_remove(parent)
        frame = parent.frames[cont]
        frame.tkraise()
        # frame.grid()

    #blue Frame
    def BlueFrame(self, container):
        pass

    #Some Functions
    def exitProgram(self):
        exit()

    # def showFrame(self, cont):
    #     #looking at the frames list at position cont
    #     frame = self.frames[cont]
    #     frame.tkraise()

    #Button functions below
    def functionRecord(self):
        pass

    def functionConvert(self):
        pass

    def functionPlay(self):
        pass

    def functionTest1(self):
        self.showFrame(StartPage)

    def functionTest2(self):
        self.showFrame(SecondPage)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        #the parent is a tk.Tk instance called root?
        tk.Frame.__init__(self,parent)
        #LARGE_FONT defined above
        label = tk.Label(self, text = "What the?")
        label.pack(pady=10, padx=10)

class SecondPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #LARGE_FONT defined above
        label = tk.Label(self, text = "Second?")
        label.pack(pady=10, padx=10)

def main():
    root = tk.Tk()
    root.title("VHS Conversion")
    # root.geometry(screen_geometry)
    #View(root)
    View(root, controller)
    root.mainloop()


main()

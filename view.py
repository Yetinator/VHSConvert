#this should make mencoder easy

import os
from menconstruct import MenConstruct
import subprocess
from pathlib import Path
import tkinter as tk

import controller
from configurations import *
from convertSettingsPage import *
from movieSelectionPage import *
from playPage import *

class View(tk.Tk):

    #pull in a few configurations
    # raw_vhs_filepath = RAW_VHS_FILEPATH
    # finished_vhs_filepath = FINISHED_VHS_FILEPATH

    # screen_geometry = SCREEN_GEOMETRY


    # def __init__(self, parent, controller):
    def __init__(self):
        self.pageList = (StartPage, PageTwo, ConvertSettingsPage, MovieSelectionPage, PlayPage)
        #Wtf is the parent here?
        # self.controller = controller
        self.appController = controller.AppController()
        tk.Tk.__init__(self)
        self.geometry(SCREEN_GEOMETRY)
        self.createInterfaceBase()
        self.title("VHS Converter")



        # how to implement frame switch
        # parent.frames = {}
        self.createFrames()
        # parent.showFrame(StartPage)

        #self.canvas.bind("")

    #Initializer Function
    def createInterfaceBase(self):
        #create layout
        self.createTopMenu()
        self.frameButtonPane = tk.Frame(self, width=200, bg="green")

        self.frameRandom = tk.Frame(self, width = 120, bg="red", relief=tk.SUNKEN)
        self.createButtonPane(self.frameButtonPane)

        self.frameButtonPane.pack(side=tk.LEFT, fill=tk.X, expand=1)
        self.frameRandom.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    #Initializer Function
    def createTopMenu(self):
        #layout for file, edit, help bar
        self.menuBar = tk.Menu(self)
        self.createFileMenu()

    #Initializer Function
    def createFileMenu(self):
        self.fileMenu = tk.Menu(self.menuBar)
        self.fileMenu.add_command(label="New")
        self.fileMenu.add_command(label="Open...")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exitProgram)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.config(menu=self.menuBar)

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
    def createFrames(self):
        self.frames = {}
        for F in (self.pageList):
            frame = F(self.frameRandom, self, self.appController)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        # self.frames = StartPage(self.frameRandom, self)
        # self.frames = PageTwo(self.frameRandom, self)
        self.showFrame(StartPage)

#Need to populate data from the Appcontroller so the view doesn't have to ask for anything
    def poplulateVariables(self):
        pass

    #variable Frames
    def showFrame(self, cont):
        #looking at the frames list at position cont
        for gone in self.frames:
            gone.grid_forget(self)
        frame = self.frames[cont]
        frame.tkraise()
        # frame.grid()


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

        #show the settings page and run some of the code
        # self.showFrame(ConvertSettingsPage)
        self.showFrame(MovieSelectionPage)

    def functionPlay(self):
        self.showFrame(PlayPage)

    def functionTest1(self):
        self.showFrame(StartPage)

    def functionTest2(self):
        self.showFrame(PageTwo)

    def convertSettings(self):
        #bad name, switch to convertSettingsPage
        self.frames[ConvertSettingsPage].refresh()
        self.showFrame(ConvertSettingsPage)

class StartPage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        #the parent is a tk.Tk instance called root?
        tk.Frame.__init__(self, parent)
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        #LARGE_FONT defined above
        label = tk.Label(self, text = "What the?")
        label.pack()

        butt = tk.Button(self, text="Change to Page 2", bg="teal", command=self.func1)
        butt2 = tk.Button(self, text="Change to Page 3", bg="cyan", command=self.func2)

        butt.pack()
        butt2.pack()

    def func1(self):
        self.tkObj.showFrame(PageTwo)

    def func2(self):
        # self.controller.showFrame(PageThree)
        pass


class PageTwo(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        tk.Frame.__init__(self, parent)
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        #LARGE_FONT defined above
        label = tk.Label(self, text = "Second?")
        label.pack()

        butt = tk.Button(self, text="Change to Start Page", bg="teal", command=self.func1)
        butt2 = tk.Button(self, text="Change to Page 3", bg="cyan", command=self.func2)

        butt.pack()
        butt2.pack()

    def func1(self):
        self.tkObj.showFrame(StartPage)

    def func2(self):
        # self.controller.showFrame(PageThree)
        pass




#start the app
#this should be run from controller actually
app = View()


app.mainloop()

#this should make mencoder easy

import os
from menconstruct import MenConstruct
import subprocess
from pathlib import Path
import tkinter as tk

import controller
from configurations import *

class View(tk.Tk):

    #pull in a few configurations
    # raw_vhs_filepath = RAW_VHS_FILEPATH
    # finished_vhs_filepath = FINISHED_VHS_FILEPATH

    # screen_geometry = SCREEN_GEOMETRY


    # def __init__(self, parent, controller):
    def __init__(self):

        #Wtf is the parent here?
        # self.controller = controller
        self.appController = controller.AppController()
        tk.Tk.__init__(self)
        self.geometry(SCREEN_GEOMETRY)
        self.createInterfaceBase()



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
        for F in (StartPage, PageTwo, ConvertSettingsPage):
            frame = F(self.frameRandom, self)
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
        self.showFrame(ConvertSettingsPage)

    def functionPlay(self):
        pass

    def functionTest1(self):
        self.showFrame(StartPage)

    def functionTest2(self):
        self.showFrame(PageTwo)

class StartPage(tk.Frame):

    def __init__(self, parent, tkObj):
        #the parent is a tk.Tk instance called root?
        tk.Frame.__init__(self, parent)
        self.tkObj = tkObj
        self.parent = parent
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

    def __init__(self, parent, tkObj):
        tk.Frame.__init__(self, parent)
        self.tkObj = tkObj
        self.parent = parent
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

class ConvertSettingsPage(tk.Frame):

    def __init__(self, parent, tkObj):
        #the parent for the above frame was an object that inherited from tk.Tk root window
        #but in this case...
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.tkObj = tkObj
        self.parent = parent
        tk.label = tk.Label(self, bg = "teal", text = "Convert Settings and Inputs")
        tk.label.pack()

        #Listbox for Movie
        self.createRawMovieListBox()

        #Listbox for Aspect Ratio
        aspectInput = tk.Listbox(self)
        aspectInput.insert(tk.END, "4/3")
        aspectInput.insert(tk.END, "16/9")
        aspectInput.insert(tk.END, "1.85/1")
        enterButton = tk.Button(self, text="Enter")
        a = aspectInput.bind("<Double-Button-1>", aspectInput.get(tk.ACTIVE))
        print(a)

        aspectInput.pack()
        enterButton.pack()


        butt = tk.Button(self, text="Change to Start Page", bg="teal", command=self.func1)
        butt.pack()

    def func1(self):
        self.tkObj.showFrame(StartPage)

    def createRawMovieListBox(self):
        self.convertListBox = tk.Listbox(self)
        self.convertListBox.bind("<Double-Button-1>", self.setMovieTitle)

        #add items to listbox
        movieList = self.tkObj.appController.getRawMovieFileList()
        for item in movieList:
            self.convertListBox.insert(tk.END, item)

        #TODO
        #createFileList

        self.convertListBox.pack()

    def setMovieTitle(self, event):
        #Todo - Move to another class...???
            widget = event.widget
            selection=widget.curselection()
            movieTitle = widget.get(selection[0])
            self.tkObj.appController.setMovieTitle(movieTitle)
            return movieTitle


# def main():
#     root = tk.Tk()
#     root.title("VHS Conversion")
#     # root.geometry(screen_geometry)
#     #View(root)
#     View(root)
#     root.mainloop()


#start the app
#this should be run from controller actually
app = View()


app.mainloop()

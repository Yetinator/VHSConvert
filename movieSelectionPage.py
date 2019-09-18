import tkinter as tk
import controller
from configurations import *
from configurationsSystem import *

listBoxWidth = LIST_BOX_WIDTH
class MovieSelectionPage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        #the parent for the above frame was an object that inherited from tk.Tk root window
        #but in this case...
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        self.boxCurrentMovieSelected = "None"

        label = tk.Label(self, bg = "teal", text = "Convert Settings and Inputs")
        label.pack(fill=tk.X, expand=1)

        #Listbox for Movie
        self.createRawMovieListBox()


        enterButt = tk.Button(self, text="Select Movie", bg="teal", command=self.enterButton)
        enterButt.pack()

    def func1(self):
        self.tkObj.showFrame(StartPage)

    def enterButton(self):
        #start collecting conversion configurations from convertSettingsPage

        # #check Critera are selected
        # aspectRatio = self.aspectRatio.get()
        # # movieChoice = self.boxCurrentMovieSelected
        movieChoice = self.convertListBox.get(self.convertListBox.curselection())
        # print(type(self.tkObj.showFrame(self.tkObj.frames[ConvertSettingsPage])))
        self.appController.setCurrentMovieSelected(movieChoice)
        self.tkObj.convertSettings()
        # if (True):
        #     #set aspect Ratio, Movie Title, other
        #     self.appController.convertMovie(movieChoice, aspectRatio)

    def refresh(self):
        self.createRawMovieListBox()


    #initiallizer Function
    def aspectRatioFrame(self):
        aspectInput = tk.Listbox(self)
        aspectInput.insert(tk.END, "4/3")
        aspectInput.insert(tk.END, "16/9")
        aspectInput.insert(tk.END, "1.85/1")
        enterButton = tk.Button(self, text="Enter")
        # a = aspectInput.bind("<Double-Button-1>", aspectInput.get(tk.ACTIVE))
        aspectInput.pack()
        enterButton.pack()

    #initiallizer Function
    def aspectRatioFrameRadioButtons(self):
        self.aspectRatio = tk.StringVar()
        for i in ("4/3", "16/9", "1.85/1"):
            tk.Radiobutton(self, text=i, variable=self.aspectRatio, value=i).pack(anchor=tk.W)

    #initiallizer Function
    def createRawMovieListBox(self):
        # self.movieSelection = tk.Label(self, bg = "yellow", text = self.boxCurrentMovieSelected)
        self.convertListBox = tk.Listbox(self, width=listBoxWidth)
        # self.convertListBox.bind("<Double-Button-1>", self.highlightMovieTitle)
        #add items to listbox
        # movieList = self.tkObj.appController.getRawMovieFileList()
        movieList = self.tkObj.appController.getUnconvertedMovieFileList()

        for item in movieList:
            self.convertListBox.insert(tk.END, item)
        #TODO
        #createFileList
        # self.movieSelection.pack()
        self.convertListBox.pack(fill=tk.X, expand=1)


    #Event
    def setMovieTitle(self, event):
        #Todo - Move to another class...???
            widget = event.widget
            selection=widget.curselection()
            movieTitle = widget.get(selection[0])
            self.tkObj.appController.setMovieTitle(movieTitle)
            return movieTitle

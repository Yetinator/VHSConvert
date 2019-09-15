import tkinter as tk
import controller
from configurations import *
from troubleshooting import *


class PlayPage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        #the parent for the above frame was an object that inherited from tk.Tk root window
        #but in this case...
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        self.boxCurrentMovieSelected = "None"
        tk.label = tk.Label(self, bg = "teal", text = "Convert Settings and Inputs")
        tk.label.pack()

        #Listbox for Movie
        self.createTheMovieListBox()

        #Listbox for Aspect Ratio
        # self.aspectRatioFrame()
        # self.aspectRatioFrameRadioButtons()

        enterButt = tk.Button(self, text="Select Movie to watch", bg="teal", command=self.enterButton)
        enterButt.pack()

    def func1(self):
        self.tkObj.showFrame(StartPage)

    def enterButton(self):
        #start collecting conversion configurations from convertSettingsPage

        # #check Critera are selected
        # aspectRatio = self.aspectRatio.get()
        # # movieChoice = self.boxCurrentMovieSelected
        movieChoice = self.watchListBox.get(self.watchListBox.curselection())
        # print(type(self.tkObj.showFrame(self.tkObj.frames[ConvertSettingsPage])))

        waldo("movieChoice ", movieChoice)
        # self.appController.setCurrentMovieSelected(movieChoice)
        # self.appController.setMovieToPlay(movieChoice)

        # self.tkObj.convertSettings()

        # if (True):
        #     #set aspect Ratio, Movie Title, other
        #     self.appController.convertMovie(movieChoice, aspectRatio)
        self.appController.playFile(movieChoice, False)



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
    def createTheMovieListBox(self):
        # self.movieSelection = tk.Label(self, bg = "yellow", text = self.boxCurrentMovieSelected)

        self.watchListBox = tk.Listbox(self)
        # self.watchListBox.bind("<Double-Button-1>", self.highlightMovieTitle)
        #add items to listbox
        if(False):
            movieList = self.tkObj.appController.getRawMovieFileList()

        else:
            movieList = self.tkObj.appController.getFinishedMovieFileList()
            print(movieList)

        for item in movieList:
            self.watchListBox.insert(tk.END, item)

        #TODO
        #createFileList
        # self.movieSelection.pack()
        self.watchListBox.pack()

    #Event
    def setMovieTitle(self, event):
        #Todo - Move to another class...???
            widget = event.widget
            selection=widget.curselection()
            movieTitle = widget.get(selection[0])
            # self.tkObj.appController.setMovieTitle(movieTitle)
            return movieTitle

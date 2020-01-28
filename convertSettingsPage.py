import tkinter as tk
import controller
from configurations import *
from configurationsSystem import *
from troubleshooting import *


class ConvertSettingsPage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        #the parent for the above frame was an object that inherited from tk.Tk root window
        #but in this case...
        self.movieChoice = False
        self.endOfFile = False
        self.endOfMovieUser = {}
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        self.boxCurrentMovieSelected = "None"

        label = tk.Label(self, bg = "teal", text = "Convert Settings and Inputs")
        label.pack()

        #Listbox for Movie
        # self.createRawMovieListBox()

        self.movieLabel = tk.Label(self, bg = "teal", text = str(self.appController.currentMovieSelected))
        self.movieLabel.pack()

        #Listbox for Aspect Ratio
        # self.aspectRatioFrame()
        self.aspectRatioFrameRadioButtons()
        self.endPositionInfo()

        enterButt = tk.Button(self, text="ENTER", bg="teal", command=self.enterButton)
        enterButt.pack()


    def func1(self):
        self.tkObj.showFrame(StartPage)

    def refresh(self):
        self.movieChoice = self.appController.currentMovieSelected
        self.movieLabel.config(text = self.movieChoice)
        self.endOfFile = self.appController.endOfFile
        self.LabelEndOfFile.config(text = self.endOfFile)

    def enterButton(self):
        #check Critera are selected
        aspectRatio = self.aspectRatio.get()
        # self.endOfMovieUser = self.inputBoxHours.get() + ":" + self.inputBoxMinutes.get() + ":" + self.inputBoxSeconds.get()
        self.endOfMovieUser["hours"] = self.inputBoxHours.get()
        self.endOfMovieUser["minutes"] = self.inputBoxMinutes.get()
        self.endOfMovieUser["seconds"] = self.inputBoxSeconds.get()
        for i in self.endOfMovieUser:
            print("wahwa " + self.endOfMovieUser[i])
        # movieChoice = self.boxCurrentMovieSelected
        # movieChoice = self.convertListBox.get(self.convertListBox.curselection())
        if (True):
            #set aspect Ratio, Movie Title, other
            self.appController.convertMovie(self.movieChoice, aspectRatio, self.endOfMovieUser)
            self.tkObj.refresh()

    def playButton(self):
        self.appController.playMovieForEndTime(self.movieChoice)


    #initiallizer Function
    # def aspectRatioFrame(self):
    #     aspectInput = tk.Listbox(self)
    #     aspectInput.insert(tk.END, "4/3")
    #     aspectInput.insert(tk.END, "16/9")
    #     aspectInput.insert(tk.END, "1.85/1")
    #     enterButton = tk.Button(self, text="Enter")
    #     # a = aspectInput.bind("<Double-Button-1>", aspectInput.get(tk.ACTIVE))
    #     aspectInput.pack()
    #     enterButton.pack()

    #initiallizer Function
    def aspectRatioFrameRadioButtons(self):
        # self.aspectRatio = tk.IntVar()
        self.aspectRatio = tk.StringVar()
        # self.aspectDictionary = []
        # for i in ("4/3", "16/9", "1.85/1"):
        #     self.aspectDictionary.append(tk.Radiobutton(self, text=i, variable=self.aspectRatio, value=i).pack(anchor=tk.W))

        self.buttonA = tk.Radiobutton(self, text="4/3", variable=self.aspectRatio, value="4/3")
        self.buttonA.pack(anchor=tk.W)
        self.buttonA.deselect()

        self.buttonB = tk.Radiobutton(self, text="16/9", variable=self.aspectRatio, value="16/9")
        self.buttonB.pack(anchor=tk.W)
        self.buttonB.select()

        self.buttonC = tk.Radiobutton(self, text="1.85/1", variable=self.aspectRatio, value="1.85/1")
        self.buttonC.pack(anchor=tk.W)
        self.buttonC.deselect()

        # self.buttonB.set("16/9")




    def endPositionInfo(self):
        label = tk.Label(self, bg = "teal", text = "End of file")
        self.LabelEndOfFile = tk.Label(self, bg = "teal", text = self.endOfFile)

        label2 = tk.Label(self, bg = "teal", text = "User defined End of Movie")

        inputFrame = tk.Frame(self)
        # inputBoxHours = tk.Entry(inputFrame, text = "Hours", textvariable = hours)
        # inputBoxMinutes = tk.Entry(inputFrame, text = "Minutes", textvariable = minutes)
        # inputBoxSeconds = tk.Entry(inputFrame, text = "Seconds", textvariable = seconds)

        self.inputBoxHours = tk.Entry(inputFrame, text = "Hours" )
        self.inputBoxMinutes = tk.Entry(inputFrame, text = "Minutes")
        self.inputBoxSeconds = tk.Entry(inputFrame, text = "Seconds")

        #this calls mplayer to navigate to the end of the movie and make finding the end awesome
        playMovie = tk.Button(self, text="Play a Clip to find the end", bg="teal", command=self.playButton)

        self.inputBoxHours.pack()
        self.inputBoxMinutes.pack()
        self.inputBoxSeconds.pack()

        label.pack()
        self.LabelEndOfFile.pack()

        label2.pack()
        inputFrame.pack()
        playMovie.pack()


        #this does not collect info from appcontroller, that should have happened on refresh
        #this populates the front end part


    #initiallizer Function
    def createRawMovieListBox(self):
        self.movieSelection = tk.Label(self, bg = "yellow", text = self.boxCurrentMovieSelected)
        self.convertListBox = tk.Listbox(self)
        # self.convertListBox.bind("<Double-Button-1>", self.highlightMovieTitle)
        #add items to listbox
        movieList = self.tkObj.appController.getRawMovieFileList()
        for item in movieList:
            self.convertListBox.insert(tk.END, item)
        #TODO
        #createFileList
        self.movieSelection.pack()
        self.convertListBox.pack()

    #Event
    def setMovieTitle(self, event):
        #Todo - Move to another class...???
            widget = event.widget
            selection=widget.curselection()
            movieTitle = widget.get(selection[0])
            self.tkObj.appController.setMovieTitle(movieTitle)
            return movieTitle

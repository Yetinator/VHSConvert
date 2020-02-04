import tkinter as tk
import controller
from configurations import *
from configurationsSystem import *
from troubleshooting import *


class DeletePage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        #the parent for the above frame was an object that inherited from tk.Tk root window
        #but in this case...
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        tk.label = tk.Label(self, bg = "teal", text = "This page lists files that should be done and ready to delete.  Delete below.")
        tk.label.pack()

        #Listbox for Movie
        self.createTheDeleteMovieListBox()

        enterButt = tk.Button(self, text="Select Movie to Delete", bg="teal", command=self.enterButton)
        enterButt.pack()

    def func1(self):
        self.tkObj.showFrame(StartPage)

    def enterButton(self):
        #start collecting conversion configurations from convertSettingsPage

        deleteMovieChoice = self.deleteMovieListBox.get(self.deleteMovieListBox.curselection())

        waldo("deleteMovieChoice ", deleteMovieChoice)
        self.appController.deleteRawMovieFileFromRawMoviePath(deleteMovieChoice)
    
    def refresh(self):
        self.createTheDeleteMovieListBox()


    #initiallizer Function
    def createTheDeleteMovieListBox(self):
        self.deleteMovieListBox = tk.Listbox(self)
        self.deleteMovieList = self.tkObj.appController.getMoviesToDelete()
        for item in self.deleteMovieList:
            self.deleteMovieListBox.insert(tk.END, item)

        self.deleteMovieListBox.pack()

    #Event
    def setMovieTitle(self, event):
        #Todo - Move to another class...???
            widget = event.widget
            selection=widget.curselection()
            movieTitle = widget.get(selection[0])
            # self.tkObj.appController.setMovieTitle(movieTitle)
            return movieTitle

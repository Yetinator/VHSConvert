import tkinter as tk
import controller
from configurations import *
from configurationsSystem import *
from troubleshooting import *


class RecordPage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        #the parent for the above frame was an object that inherited from tk.Tk root window
        #but in this case...
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        self.appController.prepComputerInput()

        label = tk.Label(self, bg = "teal", text = "Record from tape")

        boxTitle = tk.Label(self, bg = "teal", text = "MovieName no spaces")
        self.movieName = tk.Entry(self, text = "MovieName" )

        timeTitle = tk.Label(self, bg = "teal", text = "Record timeout in hours")
        self.recordTimeOut = tk.Entry(self, text = "Record timeout" )

        enterButt = tk.Button(self, text="Record", bg="teal", command=self.enterButton)



        label.pack()
        boxTitle.pack()
        self.movieName.pack()
        timeTitle.pack()
        self.recordTimeOut.pack()
        enterButt.pack()



    def enterButton(self):
        endTime = float(self.recordTimeOut.get())
        #Convert Endtime from hours
        endTime = int(endTime * 60 * 60)
        movieName = self.movieName.get()
        
        self.appController.recordVideoNow(str(movieName), endTime)



    #initiallizer Function

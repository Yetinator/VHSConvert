import tkinter as tk
import controller
from configurations import *
from configurationsSystem import *

listBoxWidth = LIST_BOX_WIDTH
class RecordPage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        #the parent for the above frame was an object that inherited from tk.Tk root window
        #but in this case...
        tk.Frame.__init__(self, parent)
        #LARGE_FONT defined above
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        #self.tvTuneOne = True handled in model
        self.movieName = "Default"


        label = tk.Label(self, bg = "teal", text = "Record a Movie Settings")
        label.pack(fill=tk.X, expand=1)

        #Listbox for Movie
        self.createMovieInput()


        enterButt = tk.Button(self, text="Start Recording Movie", bg="teal", command=self.enterButton)
        enterButt.pack()
        
        stopButton = tk.Button(self, text="Stop Recording Movie", bg="red", command=self.stopButton)
        stopButton.pack()
        
        
    def createMovieInput(self):
        #this is the inputs for the movie
        
        self.movieNameLabel = tk.Label(self, text="MoviesNameNoSpacesCamelCase")
        self.movieNameLabel.pack()
        self.movieNameInputBox = tk.Entry(self)
        self.movieNameInputBox.pack()

        self.timeOutLabel = tk.Label(self, text= "File Timeout time in minutes recomended 180 for 3 hours")
        self.timeOutLabel.pack()     
  
        self.timeOutInputBox = tk.Entry(self)
        self.timeOutInputBox.insert(tk.END, "3")
        self.timeOutInputBox.pack()
        
        
    def enterButton(self):
        self.movieName = str(self.movieNameInputBox.get()) + ".mpg"
        #Check to see if movie already exists overwrite protection
        
        self.timeout = int(self.timeOutInputBox.get())
        if (self.timeout < 1 or self.timeout > 900):
            self.timeout = false
            print("Bad timeout value")
            
        print(self.movieName)
        print(self.timeout)    
        self.appController.startRecording(self.movieName, self.timeout)
    
            
    def stopButton(self):
        self.appController.stopRecording()

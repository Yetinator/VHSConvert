from configurations import *
from configurationsSystem import *
import model
from troubleshooting import *

class AppController():

    def __init__(self):
        #Create a model defined by MenConstruct in the model.py file
        self.init_model()
        # self.getViewVariables()
        self.currentMovieSelected = False

    def init_model(self):
        self.model = model.Model()

    def refresh(self):
        #self.model.refresh()
        pass


    #Initializer Function
    def getViewVariables(self):
        #this pulls necessary info from the model and arranges it to be passed to view
        #this happens once during initallizing
        self.moviesToConvert = self.model.getRawMovieFileList()

    def getRawMovieFileList(self):
        #passes the list of movies to the frontend from the back
        return self.model.getRawMovieFileList()

    def getUnconvertedMovieFileList(self):
        raw = self.model.getRawMovieFileList()
        finished = self.model.getFinishedMovieFileList()
        temp = []
        #need handling for VHS.avi vs .mpg
        for n in range(len(finished)):
            finished[n] = finished[n][:-7]
            print(finished[n])

        raw2 = {}
        for n in range(len(raw)):
            raw2[n] = raw[n][:-4]

        for n in raw2:
            if (raw2[n] not in finished):
                temp.append(raw[n]) 
            else:
                print("IN: " + str(n))

        return temp
        
    def getMoviesToDelete(self):
        return self.model.getMoviesToDelete()


    def getFinishedMovieFileList(self):
        return self.model.getFinishedMovieFileList()

    def setMovieTitle(self, title):
        #when the view picks a title, this passes it to the model to process

        self.model.setMovieTitle(title)
        print(title)

    def setCurrentMovieSelected(self, movie):

        self.currentMovieSelected = movie
        waldo("movie in controller ", movie)
        self.model.movieConstruct(movie)
        self.endOfFile = self.model.convertSecToTime(int(self.model.end_pos_of_file)/1000)
        # self.endOfFile = self.model.end_pos_of_file

    def setMovieToPlay(self, movie):
        self.currentMovieSelected = movie
        waldo("movie in controller movie to play", movie)
        self.model.moviePlayConstruct(movie)
        # self.endOfFile = self.model.convertSecToTime(int(self.model.end_pos_of_file)/1000)
        # self.endOfFile = self.model.end_pos_of_file


    def convertMovie(self, movieChoice, aspectRatio, endOfMovieUserEntry = False):
        #prepare the movie to convert and call conversion in model
        #endOfMoviesUserEntry just became a dictionary
        endOfFile = endOfMovieUserEntry
        #endOfFile should be a string...
        if (endOfFile == False):
            endOfFile = self.model.getEndOfFile(movieChoice)

        self.model.functionConvert(movieChoice, aspectRatio, endOfFile)

    def playFile(self, movie, originalBool):
        self.model.playMovie(movie, originalBool)

    def playMovieForEndTime(self, movie):
        self.model.playMovieForEndTime(movie)
        
    def deleteRawMovieFileFromRawMoviePath(self, movie):
        self.model.deleteRawMovieFileFromRawMoviePath(movie)

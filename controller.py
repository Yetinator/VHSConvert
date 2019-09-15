from configurations import *
import model

class AppController():

    def __init__(self):
        #Create a model defined by MenConstruct in the model.py file
        self.init_model()
        # self.getViewVariables()
        self.currentMovieSelected = False

    def init_model(self):
        self.model = model.Model()



    #Initializer Function
    def getViewVariables(self):
        #this pulls necessary info from the model and arranges it to be passed to view
        #this happens once during initallizing
        self.moviesToConvert = self.model.getRawMovieFileList()

    def getRawMovieFileList(self):
        #passes the list of movies to the frontend from the back
        return self.model.getRawMovieFileList()

    def setMovieTitle(self, title):
        #when the view picks a title, this passes it to the model to process

        self.model.setMovieTitle(title)
        print(title)

    def setCurrentMovieSelected(self, movie):

        self.currentMovieSelected = movie
        self.model.movieConstruct(movie)
        self.endOfFile = self.model.convertSecToTime(int(self.model.end_pos_of_file)/1000)
        # self.endOfFile = self.model.end_pos_of_file


    def convertMovie(self, movieChoice, aspectRatio, endOfMovieUserEntry = False):
        #prepare the movie to convert and call conversion in model
        #endOfMoviesUserEntry just became a dictionary
        endOfFile = endOfMovieUserEntry
        #endOfFile should be a string...
        if (endOfFile == False):
            endOfFile = self.model.getEndOfFile(movieChoice)

        self.model.functionConvert(movieChoice, aspectRatio, endOfFile)

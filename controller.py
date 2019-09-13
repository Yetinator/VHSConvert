from configurations import *
import model

class AppController():

    def __init__(self):
        #Create a model defined by MenConstruct in the model.py file
        self.init_model()
        # self.getViewVariables()

    def init_model(self):
        self.model = model.Model()



    #Initializer Function
    def getViewVariables(self):
        #this pulls necessary info from the model and arranges it to be passed to view
        #this happens once during initallizing
        self.moviesToConvert = self.getRawMovieFileList()

        #happens at least once during start of program and anytime view needs to be repopulated
    def forwardViewVariables(self):
        #this sends necessary variables to the view.
        pass

    def getRawMovieFileList(self):
        return self.model.getRawMovieFileList()

    def setMovieTitle(self, title):
        self.model.setMovieTitle(title)
        print(title)


#Start the app - feed info to the view
# appController = AppController()
#
#
# app = View()
# app.poplulateVariables()
#
#
# app.mainloop()

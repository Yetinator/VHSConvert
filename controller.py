from configurations import *
import model

class Controller():

    def __init__(self):
        #Create a model defined by MenConstruct in the model.py file
        self.init_model()

    def init_model(self):
        self.model = model.Model()

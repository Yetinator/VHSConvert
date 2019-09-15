#this is the mencoder construct class
#sudo apt-get install mediainfo
import os
import subprocess
from pathlib import Path
import tempfile
import time

import controller
from configurations import *

#hocus pocus
mypath = "/home/brian/Videos/RawVHSFiles"
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#Configurations import more formally than above
outputHelperFilePath = VHS_OUTPUT_FILEPATH
rawVHSFilepath = RAW_VHS_FILEPATH #mypath above should be changed as it is redundant
finishedFilePath = FINISHED_VHS_FILEPATH
referanceFilePath = REFERENCE_FILES_FILEPATH
cropDetectTimeRange = MPLAYERRANGE


# Model class here, basically MenConstruct class
class Model:



    def __init__(self):
        #Things that are needed to convert a movie
        self.movieTitle = False
        self.aspect_ratio_entered = False
        self.crop_info_entered = False
        # self.end_pos_entered = False
        self.end_pos_of_file = False
        self.endPosString = False
        self.originFile = False
        self.finishedFile = False
        # self.finishedFile = referanceFilePathOutputFiles + str(self.title) + "VHS.avi"

        # self.referanceFilePathOriginalMovies = referanceFilePath

    def functionRecord(self):
        #record Function
        self.runCommand = False
        self.user = input("Name the Movie to record:  ")
        self.hours = float(input("How many Hours before timeout:  (ex:2.5, not self.hours and minutes)"))
        self.seconds = int(self.hours * 3600)
        self.command = str("timeout {sec} cat /dev/video0 > {name}.mpg").format(sec=self.seconds,name=self.user)
        # answer = os.path.isfile("pwd /try2.mpg").format(name=self.user)
        self.file = Path("{name}.mpg".format(name=self.user))
        if self.file.is_file():
            print("The self.file exists. The recording will not start.")
        else:
            print("The self.file doesn't exist. Hopefully the recording is starting")
            self.runCommand = True
        # input("waldo")
        if self.runCommand == True:
            os.system(self.command)
            input("Enter Something to quit")
            os.system("^C")

        self.stallFunction()

    def movieConstruct(self, movieChoice):
        self.movieTitle = self.convertMovieToTitle(movieChoice)
        self.setFilePaths()
        self.getEndOfFile(movieChoice)


    def functionConvert(self, movieChoice, aspectRatio, endPos):
        #convert function
        #TODO - change endOfFile input to user selected stopping point

        self.aspect_ratio_entered = aspectRatio
        # self.crop_info_entered
        self.endPosString = self.userToTimeString(endPos)
        self.setCropInfo()

        #get inputs
        #Todo the line below is redundant
        # self.end_pos_of_file = self.end_pos_entered #end position of file is a weird concept because nothing is finalized until the convert function is called

        #Test inputs
        print(self.movieTitle)
        print(self.aspect_ratio_entered )
        print(self.crop_info_entered)#
        print(self.end_pos_of_file )
        print(self.endPosString)
        print(self.originFile)#
        print(self.finishedFile)
        if(self.testInputValuesForMencoder()):
            print("about to run mencoder")
            self.runMencoder()
            print("Done with mencoder")



    def functionPlay():
        #Play Function
        self.stallFunction()

    def functionTest1():
        #test
        print("test Function")
        self.user = input("The self.file name: ")
        #mediainfo --Inform="General;%Duration%" try2.mpg
        # self.temp = os.system('mediainfo --Inform="General;%Duration%" ' + str(self.user) + ".mpg")
        self.temp = os.popen('mediainfo --Inform="General;%Duration%" ' + str(self.user) + ".mpg").read()
        self.temp = round(float(self.temp) / 1000,0)
        print("self.temp as rounded " + str(self.temp))


    def functionTest2():
        #test2
        print("test functionConvert")
        print("blackframe test")
        self.user = input("The self.file name: ")
        #mediainfo --Inform="General;%Duration%" try2.mpg
        os.system('mplayer ' + str(self.user) + ".mpg " + "-vf blackframe -benchmark -nosound -vo null > blackframe.txt")
        file_object = open("blackframe.txt", 'r')
        print("fileobject created")
        for line in file_object:
            if "vf_blackframe" in line:
                self.temp = line.split("vf_blackframe:")
                temp2 = self.temp[1].split(", ")
                print(temp2[0])





    def stallFunction(self):
        #literally stalls the function
        continue1 = True
        continue1 = input("This is the Stall Function.  Press a key")
        while continue1 == True:
            sleep(5)

    def exitProgram():
        exit()

    #helper functions
    # def createFileList():
    #     theList = []
    #     a = referanceFilePathOriginalMovies
    #     for item in onlyfiles:
    #         theList.append(item)
    #
    #     return theList

    def getRawMovieFileList(self):
        theList = []
        # a = self.referanceFilePathOriginalMovies
        for item in onlyfiles:
            theList.append(item)
        return theList

    def setMovieTitle(self, movie):
        print("In the thing")

    #Conversion Helper Functions
    def setCropInfo(self):
        # command = "mplayer " + self.originFile + " -vf cropdetect -benchmark -nosound -vo null -ss {} -endpos {}".format(cropDetectTimeRange[0], cropDetectTimeRange[1])
        command = "mplayer " + self.originFile + " -vf cropdetect -benchmark -nosound -vo null -endpos {}".format(cropDetectTimeRange[1])
        command += " | tee " + outputHelperFilePath + "movieData.txt"
        print(command)
        output = os.system(command)
        #LOTR example should be 720:480?
        print("Pausing")
        time.sleep(2)

        #extract data from mplayer
        #open mplayers cropdetect output file
        self.file_object = open(outputHelperFilePath + "movieData.txt", 'r')
        self.cropStringValue=["",0]
        for line in self.file_object:
            #Read a line
            #extract actual crop value from file
            if "-vf crop=" in line:
                temp = line.split("crop=")
                cropStringInstance = temp[1].split(")")
                if str(cropStringInstance[0]) != str(self.cropStringValue[0]):
                    #compare instance to existing
                    #todo - would it be better to use an average or median here?
                    self.cropStringValue[0] = cropStringInstance[0]
                    self.cropStringValue[1] = self.cropStringValue[1] + 1

        self.crop_info_entered = self.cropStringValue[0]

        # #treat it as a string
        # output = os.system(command)
        # print(output)
        # self.cropStringValue=["",0]
        # for line in output:
        #     #Read a line
        #     #extract actual crop value from file
        #     if "-vf crop=" in line:
        #         temp = line.split("crop=")
        #         cropStringInstance = temp[1].split(")")
        #         if str(cropStringInstance[0]) != str(self.cropStringValue[0]):
        #             #compare instance to existing
        #             #todo - would it be better to use an average or median here?
        #             self.cropStringValue[0] = cropStringInstance[0]
        #             self.cropStringValue[1] = self.cropStringValue[1] + 1
        # print("exiting setCropInfo")

    def getEndOfFile(self, movieChoice):
        movieFilePath = rawVHSFilepath + movieChoice
        temp = os.popen('mediainfo --Inform="General;%Duration%" ' + str(movieFilePath)).read()
        self.totalFileDurationSec = round(float(temp) / 1000,0)
        # print("temp as rounded " + str(temp))
        self.end_pos_of_file = temp
        return str(temp)

    def convertMovieToTitle(self, movieChoice):
        if (movieChoice[-4:] == ".mpg"):
            print("yeah")
            return movieChoice[:-4]
        else:
            return False

    def setFilePaths(self):
        self.originFile = rawVHSFilepath + str(self.movieTitle) + ".mpg"
        self.finishedFile = finishedFilePath + str(self.movieTitle) + "VHS.avi"

    def testInputValuesForMencoder(self):
                # self.movieTitle = False
                # self.aspect_ratio_entered = False
                # self.crop_info_entered = False
                # self.end_pos_entered = False
                # self.end_pos_of_file = False
                #
                # self.originFile = False
        if(self.movieTitle and self.aspect_ratio_entered and self.crop_info_entered and self.originFile and self.finishedFile):
            return True

    def convertSecToTime(self, time_number):
        #Starts as a number in seconds turns to time string
        time_string = str(time_number)
        h = int(time_number)//3600
        time_number = time_number % 3600
        m = int(time_number)//60
        time_number = time_number % 60
        s = int(time_number)
        #convert to string
        if(h<10):
            h = str(0) + str(h)
        else:
            h= str(h)
        if(m<10):
            m = str(0) + str(m)
        else:
            m = str(m)
        if(s<10):
            s=str(0) +str(s)
        else:
            s=str(s)
        #self.d= h + ":" + m + ":" + s
        return str(h) + ":" + str(m) + ":" + str(s)

    def userToTimeString(self, user):
        #test user values and make a proper string
        #starts as a dictionary of hours, minutes, seconds
        print(type(int(user["hours"])) is int)
        if(type(int(user["hours"])) is int and type(int(user["minutes"])) is int and type(int(user["seconds"])) is int ):
            hours = (user["hours"])

            minutes = int(user["minutes"])
            if int(minutes) >= 60:
                hours += minutes / 60
                minutes = minutes % 60

            seconds = int(user["seconds"])
            if int(seconds) > 60:
                minutes += seconds / 60
                seconds = seconds % 60

            return str(hours) + ":" + str(minutes) + ":" + str(seconds)

        else:
            print("bad user string")
            return False

    def runMencoder(self):
        # mencoderCommand = "mencoder {originalFile} -oac mp3lame -lavcopts vcodec=msmpeg4v2:aspect={aspectValue} -ovc lavc -lavcopts vbitrate=2000000 -vf crop={cropValue},scale=512:384 -endpos {endPos} -o {finishedFileThis}".format(originalFile=str(self.originFile),aspectValue=str(self.aspect_ratio_entered),cropValue=str(self.crop_info_entered),endPos=str(self.endPosString),finishedFileThis=str(self.finishedFile))
        # self.crop_info_entered = "720:480:0:0"
        mencoderCommand = "mencoder {originalFile} -oac mp3lame -lavcopts vcodec=msmpeg4v2:aspect={aspectValue} -ovc lavc -lavcopts vbitrate=2000000 -vf crop={cropValue},scale=512:384 -endpos {endPos} -o {finishedFileThis}".format(originalFile=str(self.originFile),aspectValue=str(self.aspect_ratio_entered),cropValue=str(self.crop_info_entered),endPos=str(self.endPosString),finishedFileThis=str(self.finishedFile))

        print(mencoderCommand)
        time.sleep(2)
        # input(mencoderCommand)
        os.system(mencoderCommand)





class MenConstruct:

    #the first initiallizer is devalued and only here for referance
    def __init__(self, title):
        self.aspectRatioValue = "16/9"

        #self.title =  input("Enter a movieTitle: ")
        self.title = title[:-4]

        self.set_file_paths()
        self.set_crop_info()
        self.set_end_pos()
        self.set_aspect_ratio()
        self.run_mencoder()
        #find file in filesystem
        #run mplayer
        #mplayer $MOVIENAME.mpg -vf cropdetect -ss 00:00:07 -endpos 00:00:03

    def __init__(self):

        #set some basic settings
        self.set_file_paths()

        #Manditory List of things
        self.crop_info_entered = False
        self.end_pos_entered = False
        self.aspect_ratio_entered = False


    def set_file_paths(self):
        self.originFile = referanceFilePath + str(self.title) + ".mpg"
        self.finishedFile = referanceFilePathOutputFiles + str(self.title) + "VHS.avi"

    def set_crop_info(self):
        command = "mplayer " + self.originFile + " -vf cropdetect -benchmark -nosound -vo null -ss {} -endpos {}".format(MPLAYERRANGE[0], MPLAYERRANGE[1])
        output = os.system(command + " > movieData.txt")

        #extract data from mplayer
        #open mplayers cropdetect output file
        self.file_object = open("movieData.txt", 'r')
        self.cropStringValue=["",0]
        for line in self.file_object:
            #Read a line
            #extract actual crop value from file
            if "-vf crop=" in line:
                temp = line.split("crop=")
                cropStringInstance = temp[1].split(")")
                if str(cropStringInstance[0]) != str(self.cropStringValue[0]):
                    #compare instance to existing
                    #todo - would it be better to use an average or median here?
                    self.cropStringValue[0] = cropStringInstance[0]
                    self.cropStringValue[1] = self.cropStringValue[1] + 1
        print("exiting set_crop_info")

    def set_end_pos(self):
        #First get eof
        #mediainfo --Inform="General;%Duration%" try2.mpg
        # temp = os.system('mediainfo --Inform="General;%Duration%" ' + str(user) + ".mpg")


        self.endPosition = self.end_position_automatically()
        #second get blackscreen data... will need to analyze file to decide the end of the credits

    def find_end_pos(self):
        temp = os.popen('mediainfo --Inform="General;%Duration%" ' + str(self.originFile)).read()
        self.totalFileDurationSec = round(float(temp) / 1000,0)
        print("temp as rounded " + str(temp))
        return str(temp)


    def run_mencoder(self):
        #run mencoder
        mencoderCommand = "mencoder {originalFile} -oac mp3lame -lavcopts vcodec=msmpeg4v2:aspect={aspectValue} -ovc lavc -lavcopts vbitrate=2000000 -vf crop={cropValue},scale=512:384 -endpos {endPos} -o {finishedFileThis}".format(originalFile=str(self.originFile),aspectValue=str(self.aspectRatioValue),cropValue=str(self.cropStringValue[0]),endPos=str(self.endPosition),finishedFileThis=str(self.finishedFile))
        a = input("waiting")
        input(mencoderCommand)
        os.system(mencoderCommand)

    def end_position_manually(self):
        #"00:00:03"
        valuePass = False
        print("The duration of the video is :")
        x = self.totalFileDurationSec
        print(str(x))
        timestring = self.convertSecToTime(x)
        print(timestring)
        temp = input("what is the end time in hh:mm:ss ")
        testingValuesList = temp.split(":")
        for item in testingValuesList:
            if len(item) == 2:
                if int(item) < 100:
                    if int(item) > 9:
                        valuePass = True
        if valuePass == True:
            return temp
        else:
            print("bad endpPos value!!!!!")
            return "00:00:01"

    def end_position_automatically(self):
        #"00:00:03"
        valuePass = False

        x = self.totalFileDurationSec

        timestring = self.convertSecToTime(x)
        print(timestring)
        return timestring


    def set_aspect_ratio(self, choice):
        #updated for GUI
        #accepts choice as a string.  It must match an available option

        choice = choice
        if choice == "4/3":
            self.aspectRatioValue = "4/3"
        elif choice == "16/9":
            self.aspectRatioValue = "16/9"
        elif choice == "1.85/1":
            self.aspectRatioValue = "1.85/1"
        else:
            self.aspectRatioValue = "16/9"

    def convertSecToTime(self, time_number):
        time_string = str(time_number)
        h = int(time_number)//3600
        time_number = time_number % 3600
        m = int(time_number)//60
        time_number = time_number % 60
        s = int(time_number)
        #convert to string
        if(h<10):
            h = str(0) + str(h)
        else:
            h= str(h)
        if(m<10):
            m = str(0) + str(m)
        else:
            m = str(m)
        if(s<10):
            s=str(0) +str(s)
        else:
            s=str(s)
        #self.d= h + ":" + m + ":" + s
        return str(h) + ":" + str(m) + ":" + str(s)

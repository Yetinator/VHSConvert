#this is the mencoder construct class
#sudo apt-get install mediainfo
import os
import subprocess
import signal
from pathlib import Path
import tempfile
import time
from troubleshooting import *

import controller
from configurations import *
from configurationsSystem import *

#hocus pocus
mypath = RAW_VHS_FILEPATH
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#Configurations import more formally than above
outputHelperFilePath = VHS_OUTPUT_FILEPATH
rawVHSFilepath = RAW_VHS_FILEPATH #mypath above should be changed as it is redundant
finishedFilePath = FINISHED_VHS_FILEPATH
referanceFilePath = REFERENCE_FILES_FILEPATH
cropDetectTimeRange = MPLAYERRANGE

onlyfiles = [f for f in listdir(rawVHSFilepath) if isfile(join(rawVHSFilepath, f))]
# self.finishedFiles = [i for i in listdir(finishedFilePath) if isfile(join(finishedFilePath, i))]

# Model class here, basically MenConstruct class
class Model:



    def __init__(self):
        #Things that are needed to convert a movie
        self.finishedFiles = [i for i in listdir(finishedFilePath) if isfile(join(finishedFilePath, i))]
        self.movieTitle = False
        self.aspect_ratio_entered = False
        self.crop_info_entered = False
        # self.end_pos_entered = False
        self.end_pos_of_file = False
        self.endPosString = False
        self.originFile = False
        self.finishedFile = False
        self.movieSuffix = False
        self.playFile = False
        self.recordProcess = False
        self.tvtune = False
        self.isRecording = False
        self.startTime = False
        self.finishTime = False
        # self.finishedFile = referanceFilePathOutputFiles + str(self.title) + "VHS.avi"

        # self.referanceFilePathOriginalMovies = referanceFilePath

    def refresh(self):
        self.finishedFiles = [i for i in listdir(finishedFilePath) if isfile(join(finishedFilePath, i))]
        onlyfiles = [f for f in listdir(rawVHSFilepath) if isfile(join(rawVHSFilepath, f))]

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

    def moviePlayConstruct(self, movieChoice):
        self.movieTitle = self.convertMovieToTitle(movieChoice)
        self.setFilePaths()
        # self.getEndOfFile(movieChoice)


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

    def getFinishedMovieFileList(self):
        theList = []
        for item in self.finishedFiles:
            theList.append(item)
        return theList
        
    def getMoviesToDelete(self):
        #self.refresh()
        deleteList = []
        raw = self.getRawMovieFileList()
        finished = self.getFinishedMovieFileList()
        temp = []
        #need handling for VHS.avi vs .mpg
        for n in range(len(finished)):
            finished[n] = finished[n][:-7]
            print(finished[n])

        raw2 = {}
        for n in range(len(raw)):
            raw2[n] = raw[n][:-4]

        for n in raw2:
            if (raw2[n] in finished):
                temp.append(raw[n]) 
            else:
                print("IN: " + str(n))
                
        return temp

    def isFileWriteSafe(self, file):
        theFile = self.removeWhateverPrefixAndSuffix(file)
        finishedList = []
        list = self.getFinishedMovieFileList()
        for i in list:
            finishedList.append(self.removeWhateverPrefixAndSuffix(i))

        if theFile in finishedList:
            print("already exists")
            return False

        elif (theFile not in finishedList):
            return True


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
        # movieFilePath = rawVHSFilepath + movieChoice
        # waldo("movieFilePath", movieFilePath)
        #on a different system having trouble with usingPopopen?
        #desktop version below

        # temp = os.popen('mediainfo --Inform="General;%Duration%" ' + str(movieFilePath)).read()

        #change for laptop
        temp = os.popen('mediainfo --Inform="General;%Duration%" ' + str(movieFilePath)).read()
        # waldo("temp", temp)

        self.totalFileDurationSec = round(float(temp) / 1000,0)
        # print("temp as rounded " + str(temp))
        self.end_pos_of_file = temp
        return str(temp)

    def convertMovieToTitle(self, movieChoice):
        movieTitle = False

        if (movieChoice[-4:] == ".mpg"):
            self.movieSuffix = ".mpg"
            movieTitle = movieChoice[:-4]


        if (movieChoice[-4:] == ".avi"):
            self.movieSuffix = ".avi"
            movieTitle = movieChoice[:-4]

        if (movieTitle[-3:] == "VHS"):
            movieTitle = movieTitle[:-3]

        return movieTitle

    def removeWhateverPrefixAndSuffix(self, fullInput):
        #I guess this could be either a filepath or a movie
        #I guess this is redundant on converMovieToTitle and could in some way be combined.
        splitList = fullInput.split("/")
        input = splitList[-1]
        output = False

        if (input[-4:] == ".mpg"):
            output = input[:-4]

        if (input[-4:] == ".avi"):
            self.movieSuffix = ".avi"
            output = input[:-4]

        if (output[-3:] == "VHS"):
            output = output[:-3]

        # waldo("output", output)

        return output



    def setFilePaths(self):
        self.originFile = rawVHSFilepath + str(self.movieTitle) + ".mpg"
        self.finishedFile = finishedFilePath + str(self.movieTitle) + "VHS.avi"

    def setPlayFilePath(self, movie, originalBool = False):
        #change movie to movieTitle
        movieTitle = self.convertMovieToTitle(movie)

        if (originalBool == False):
            self.playFile = rawVHSFilepath + str(movieTitle) + ".mpg"
        if (originalBool == True):
            self.playFile = finishedFilePath + str(movieTitle) + ".avi"


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

        #check for overwrite
        safe = self.isFileWriteSafe(self.finishedFile)

        if(safe):
            mencoderCommand = "mencoder {originalFile} -oac mp3lame -lavcopts vcodec=msmpeg4v2:aspect={aspectValue} -ovc lavc -lavcopts vbitrate=2000000 -vf crop={cropValue},scale=512:384 -endpos {endPos} -o {finishedFileThis}".format(originalFile=str(self.originFile),aspectValue=str(self.aspect_ratio_entered),cropValue=str(self.crop_info_entered),endPos=str(self.endPosString),finishedFileThis=str(self.finishedFile))
            print(mencoderCommand)
            time.sleep(2)
            # input(mencoderCommand)
            os.system(mencoderCommand)

    def playMovie(self, movie, originalBool = False):
        #this needs handling for avg file
        self.setPlayFilePath(movie, originalBool)
        playCommand = "mplayer " + str(self.playFile)
        os.system(playCommand)

    def playMovieForEndTime(self, movie):
        # self.setFilePaths()
        self.movieConstruct(movie)
        endTime = int(self.getEndOfFile(movie)) / 1000
        print("endTime " + str(endTime))
        startTime = "01:30:00"
        if endTime < 10500:
            startTime = int(endTime * .94)
        #startTime = 20
        print("start time looks like this : " + str(startTime))
        playCommand = "mplayer " + str(self.originFile) + " -ss {startTime} -osdlevel 2 -fs ".format(startTime = str(startTime))
        #playCommand = "mplayer " + str(self.originFile) + " -sstep 5 -ss {startTime} -osdlevel 2 -fs ".format(startTime = str(startTime))
        #playCommand = "mplayer " + str(self.originFile) + " -osdlevel 2 -fs "
        os.system(playCommand)


        # mplayer try2.mpg -fs -osdlevel 2^C
        #osdlevel means timer
        #arrow keys skip time
        #-ss start time
        # -sstep skips frames in seconds
        
    def deleteRawMovieFileFromRawMoviePath(self, movie):  
        deleteFile = rawVHSFilepath + str(movie)
        deleteCommand = "rm " + str(deleteFile)
         
    
        print("In model trying to delete: " + str(deleteCommand))
        os.system(deleteCommand)
        self.refresh()
        
        
    def startRecording(self, movieTitle, timeout):
        filepath = rawVHSFilepath + str(movieTitle)
        if self.tvtune == False:
            tvtuner = os.system("ivtv-tune -c3")
            self.tvtune=True
            print("tv tune status? " + str(tvtuner))
        recordCommand = "cat /dev/video0 > {filename}".format(filename=filepath)
        #recordCommand = "timeout {time}m cat /dev/video0 > {filename}".format(time=int(timeout), filename=filepath)
        self.recordProcess = subprocess.Popen(recordCommand, shell=True, preexec_fn=os.setsid)
        timer = str(timeout) + "m"
        timeInSeconds = int(timeout) * 60
        self.startTime = time.time()
        self.finishTime = self.startTime + timeInSeconds
        self.isRecording = True
        #time.sleep(timeout * 60)

        #self.stopRecording()
        #self.recordProcess = subprocess.Popen(recordCommand, shell=True)
        
    def stopRecording(self):
        os.killpg(os.getpgid(self.recordProcess.pid), signal.SIGTERM)
        self.isRecording = False
        #subprocess.Popen.kill(self.recordProcess)
        
    def doInLoop(self):
        if (self.isRecording == True):
            thisTime = time.time()
            if thisTime > self.finishTime:
                self.stopRecording()
                self.isRecording = False
                print("Stop Recording at : " + str(thisTime - self.startTime))
            else:
                thisTime = time.time()
                print("Is Recording Time = " + str(round(thisTime - self.startTime))) 
            
        
        

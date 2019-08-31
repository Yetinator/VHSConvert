#this is the mencoder construct class
#sudo apt-get install mediainfo
import os
import subprocess
from pathlib import Path
import tempfile


# referanceFilePath = "smb://mediacenter/public/Movies/"
# MPLAYERRANGE = ["00:10:00", "00:00:15"]

referanceFilePath ="/home/brian/Videos/RawVHSFiles/"
referanceFilePathOutputFiles = "/home/brian/Videos/FinishedVHSFiles/"
#TODO fix this referance path and the one in main to match
MPLAYERRANGE = ["00:00:07", "00:00:03"] #the second value here isn't a timestamp it is a duration



class MenConstruct:
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
        temp = os.popen('mediainfo --Inform="General;%Duration%" ' + str(self.originFile)).read()
        self.totalFileDurationSec = round(float(temp) / 1000,0)
        print("temp as rounded " + str(temp))

        self.endPosition = self.end_position_manually()
        #second get blackscreen data... will need to analyze file to decide the end of the credits


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

    def set_aspect_ratio(self):
        print("Pick aspect ratio: ")
        print("1)  4/3")
        print("2)  16/9")
        print("3)  even wider!")
        choice = input("Select: ")
        if choice == "1":
            self.aspectRatioValue = "4/3"
        elif choice == "2":
            self.aspectRatioValue = "16/9"
        elif choice == "3":
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

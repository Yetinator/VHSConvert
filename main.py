#this should make mencoder easy
#create a really basic commandline menu with eventloop?
import os
from menconstruct import MenConstruct
import subprocess
from pathlib import Path

global PROGRAMRUNNING
PROGRAMRUNNING = True

#Enter a start folder
#Enter a completed folder
#Path gets sketch on old computer so...

def function1():
    #record Function
    runCommand = False
    user = input("Name the Movie to record:  ")
    hours = float(input("How many Hours befor timeout:  (ex:2.5, not hours and minutes)"))
    seconds = int(hours * 3600)
    command = str("timeout {sec} cat /dev/video0 > {name}.mpg").format(sec=seconds,name=user)
    # answer = os.path.isfile("pwd /try2.mpg").format(name=user)
    file = Path("{name}.mpg".format(name=user))
    if file.is_file():
        print("The file exists. The recording will not start.")
    else:
        print("The file doesn't exist. Hopefully the recording is starting")
        runCommand = True
    # input("waldo")
    if runCommand == True:
        os.system(command)
        input("Enter Something to quit")
        os.system("^C")

    stallFunction()

def function2():
    #convert function
    theMovie = MenConstruct()

    stallFunction()

def function3():
    #Play Function
    stallFunction()

def function4():
    #test
    print("test Function")
    user = input("The file name: ")
    #mediainfo --Inform="General;%Duration%" try2.mpg
    # temp = os.system('mediainfo --Inform="General;%Duration%" ' + str(user) + ".mpg")
    temp = os.popen('mediainfo --Inform="General;%Duration%" ' + str(user) + ".mpg").read()
    temp = round(float(temp) / 1000,0)
    print("temp as rounded " + str(temp))
    stallFunction()

def function5():
    #test2
    print("test Function2")
    print("blackframe test")
    user = input("The file name: ")
    #mediainfo --Inform="General;%Duration%" try2.mpg
    os.system('mplayer ' + str(user) + ".mpg " + "-vf blackframe -benchmark -nosound -vo null > blackframe.txt")
    file_object = open("blackframe.txt", 'r')
    print("fileobject created")
    for line in file_object:
        if "vf_blackframe" in line:
            temp = line.split("vf_blackframe:")
            temp2 = temp[1].split(", ")
            print(temp2[0])
    #
    # temp = round(float(temp) / 1000,0)
    # print("temp as rounded " + str(temp))

    stallFunction()

def function6():
    print("function6")
    stallFunction()

def function7():
    print("function7")
    stallFunction()

def function8():
    print("function8")
    stallFunction()

def quit():
    global PROGRAMRUNNING
    PROGRAMRUNNING = False

def stallFunction():
    continue1 = True
    continue1 = input("Press any key to continue")
    while continue1 == True:
        sleep(5)


# options = {'this': fuction1, 'that':function2, 'the other':function3}
options = ['Record','Convert','Play','Test','Test2','quit']

def mainScreen(message = None):
    global PROGRAMRUNNING
    os.system("clear")
    print(message)
    theMessage = ""
    for option in options:
        print(str(options.index(option) + 1) + ":  " + option)

    uInput = input("Select: ")
    print(uInput)


    try:
        uInput = int(uInput)
        if uInput == 1:
            function1()
        if uInput == 2:
            function2()
        if uInput == 3:
            function3()
        exitInput = len(options)
        if uInput == 4:
            function4()
        if uInput == 5:
            function5()

        if uInput == len(options):
            quit()
    except:
        theMessage = "Pick a correct value"

    if PROGRAMRUNNING == True:
        mainScreen(theMessage)





mainScreen()

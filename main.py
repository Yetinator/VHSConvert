#this should make mencoder easy
#create a really basic commandline menu with eventloop?
import os
from menconstruct import MenConstruct
import subprocess
from pathlib import Path
import tkinter as tk

#test code
mypath = "/home/brian/Videos/RawVHSFiles"
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

global PROGRAMRUNNING
PROGRAMRUNNING = True

referanceFilePathOriginalMovies = ""

#Enter a start folder
#Enter a completed folder
#Path gets sketch on old computer so...

def functionRecord():
    #record Function
    runCommand = False
    user = input("Name the Movie to record:  ")
    hours = float(input("How many Hours before timeout:  (ex:2.5, not hours and minutes)"))
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


def functionConvert(event):
    #convert function
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    movieTitle = value

    #temp tk box for aspect ratio
    selectBoxConversion = tk.Tk()
    aspectInput = tk.Listbox(selectBoxConversion)
    aspectInput.insert(tk.END, "4/3")
    aspectInput.insert(tk.END, "16/9")
    aspectInput.insert(tk.END, "1.85/1")
    enterButton = tk.Button(selectBoxConversion, text="Enter")
    a = aspectInput.bind("<Double-Button-1>", aspectInput.get(tk.ACTIVE))
    print(a)

    aspectInput.pack()
    enterButton.pack()

    #print("element " + element)


    theMovie = MenConstruct(movieTitle)
    #use variable setters for stuff here


    stallFunction()

def functionPlay():
    #Play Function
    stallFunction()

def functionTest1():
    #test
    print("test Function")
    user = input("The file name: ")
    #mediainfo --Inform="General;%Duration%" try2.mpg
    # temp = os.system('mediainfo --Inform="General;%Duration%" ' + str(user) + ".mpg")
    temp = os.popen('mediainfo --Inform="General;%Duration%" ' + str(user) + ".mpg").read()
    temp = round(float(temp) / 1000,0)
    print("temp as rounded " + str(temp))
    stallFunction()

def functionTest2():
    #test2
    print("test functionConvert")
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

#def quit():
#    global PROGRAMRUNNING
#    PROGRAMRUNNING = False

def stallFunction():
    continue1 = True
    continue1 = input("Press any key to continue")
    while continue1 == True:
        sleep(5)

def exitProgram():
    exit()

#helper functions
def createFileList():
    theList = []
    a = referanceFilePathOriginalMovies
    for item in onlyfiles:
        theList.append(item)

    return theList




# options = {'this': fuction1, 'that':functionConvert, 'the other':functionPlay}
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
            functionRecord()
        if uInput == 2:
            functionConvert()
        if uInput == 3:
            functionPlay()
        exitInput = len(options)
        if uInput == 4:
            functionTest1()
        if uInput == 5:
            functionTest2()

        if uInput == len(options):
            quit()
    except:
        theMessage = "Pick a correct value"

    if PROGRAMRUNNING == True:
        mainScreen(theMessage)


#let's make a gui!
root = tk.Tk()
root.geometry("300x900")

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)

#top menu
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitProgram)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...")

#Da! Buttons! and inputs and the like
recordButton = tk.Button(root, text="Record", command=functionRecord)
convertListbox = tk.Listbox(root)
#convertButton = tk.Button(root, text="Convert", command=lambda convertListbox=convertListbox: functionConvert(tk.ANCHOR))
convertButton = tk.Button(root, text="Convert")
convertListbox.bind("<Double-Button-1>", functionConvert)
playButton = tk.Button(root, text="Play", command=functionPlay)
testButton = tk.Button(root, text="test", command=functionTest1)
testButton2 = tk.Button(root, text="test2", command=functionTest2)
exitButton = tk.Button(root, text="Exit!", command=exitProgram)

#Listbox.insert adds items
for item in createFileList():
    convertListbox.insert(tk.END, item)

#Pack your bags
recordButton.pack()
convertButton.pack()
convertListbox.pack()
playButton.pack()
testButton.pack()
testButton2.pack()
exitButton.pack()



root = tk.mainloop()
#mainScreen()

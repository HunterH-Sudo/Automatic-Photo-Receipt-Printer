import printer
import time 
import os
import dirscanner
from threading import Thread
import threading

RecevingFile = False
fileChanged = False
activationTime = 0
Waiting = True
printing = False
WaitingText = "Waiting for new file"
WaitingLength = 23
RecevingText = "Receving File"
RecevingLength = 19


def filescan():
    global Waiting, WaitingText, WaitingLength, RecevingLength, RecevingText, activationTime, fileChanged, RecevingFile
    while True:
        if dirscanner.detect_file_changes("test.jpg") == True:
            Waiting = False
            activationTime = time.time()
            fileChanged = True
        else:
            pass
         
def Print():
    global fileChanged
    global activationTime
    global Waiting
    global printing
    while True:
        time.sleep(1)
        currentTime = time.time()
        if fileChanged == True:
                if (currentTime-activationTime) >= 3:
                    printing = True
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Prepairing to print")
                    printer.Print(r"C:\SMB\test.jpg")
                    activationTime = 0
                    fileChanged = False
                    printing = False
                    Waiting = True
        else:
            pass


thread1 = Thread(target=filescan)
thread2 = Thread(target=Print)
Thread.start(thread1)
Thread.start(thread2)

while True:
    if fileChanged == False and Waiting == True:
        if len(WaitingText) >= WaitingLength:
            os.system('cls' if os.name == 'nt' else 'clear')
            WaitingText = "Waiting for new file"
            print(WaitingText)
        else:
            WaitingText += '.'
            os.system('cls' if os.name == 'nt' else 'clear')
            print(WaitingText)
        time.sleep(1)

    if fileChanged == True and printing == False:
        if len(RecevingText) >= RecevingLength:
            RecevingText = "Receving File"
            os.system('cls' if os.name == 'nt' else 'clear')
            print (RecevingText)
        else:
            RecevingText += '.'
            os.system('cls' if os.name == 'nt' else 'clear')
            print(RecevingText)
        time.sleep(1)
    




import printer
import time 
import os
import dirscanner
from threading import Thread

RecevingFile = False
fileChanged = 0
activationTime = 0
Waiting = True
WaitingText = "Waiting for new file"
WaitingLength = 23
RecevingText = "Recevinng File"
RecevingLength = 19

class FileScanner(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        global Waiting, WaitingText, WaitingLength, RecevingLength, RecevingText, activationTime, fileChanged, RecevingFile
        while True:
            if dirscanner.detect_file_changes("test.jpg") == True:
                Waiting = False
                activationTime = time.time()
                fileChanged = 1
                RecevingFile = True
                if len(RecevingText) >= RecevingLength:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    RecevingText = "Receving File"
                    print(RecevingText)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    RecevingText += '.'
                    print(RecevingText)
            if dirscanner.detect_file_changes("test.jpg") == False and Waiting == True:
                RecevingFile = False
                if len(WaitingText) >= WaitingLength:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    WaitingText = "Waiting for new file"
                    print(WaitingText)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    WaitingText += '.'
                    print(WaitingText)


class PrintFile(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()          
    def run(self):
            global fileChanged
            global activationTime
            global Waiting
            while True:
                currentTime = time.time()
                if fileChanged == 1:
                    if (currentTime-activationTime) >= 1.5:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Prepairing to print")
                        printer.PrntNoFail(r"C:\SMB\test.jpg")
                        activationTime = 0
                        fileChanged = 0
                        Waiting = True
                        


FileScanner()
PrintFile()

while True:
    pass

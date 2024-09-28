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


def filescan(): #Configue directoy scanner and trigger for printer
    global Waiting, WaitingText, WaitingLength, RecevingLength, RecevingText, activationTime, fileChanged, RecevingFile
    while True:
        if dirscanner.detect_file_changes("test.jpg") == True:
            Waiting = False
            activationTime = time.time()
            fileChanged = True
        else:
            pass
         
def Print(): # Configure printer and activation trigger
    global fileChanged, activationTime, Waiting, printing
    while True:
        time.sleep(1)
        currentTime = time.time()
        if fileChanged == True: # Only run when the my file is changed
                if (currentTime-activationTime) >= 3: # Only tun when 3 seconds has passed
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


#Run functions as threads
thread1 = Thread(target=filescan)
thread2 = Thread(target=Print)
Thread.start(thread1)
Thread.start(thread2)

while True: # Simple loop to print what script is currently working on

    if fileChanged == False and Waiting == True: # Only run when waiting for file
        if len(WaitingText) >= WaitingLength: # If string is too long reset it
            os.system('cls' if os.name == 'nt' else 'clear')
            WaitingText = "Waiting for new file"
            print(WaitingText)
        else: # Print WaitingText and add dot to the end
            WaitingText += '.'
            os.system('cls' if os.name == 'nt' else 'clear')
            print(WaitingText)
        time.sleep(1)

    if fileChanged == True and printing == False: # Only run when receving a file
        if len(RecevingText) >= RecevingLength: # If string is too long reset it
            RecevingText = "Receving File"
            os.system('cls' if os.name == 'nt' else 'clear')
            print (RecevingText)
        else: #Print ReceingText and add dot to the end
            RecevingText += '.'
            os.system('cls' if os.name == 'nt' else 'clear')
            print(RecevingText)
        time.sleep(1)
    




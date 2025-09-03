import printer
import time 
import os
import dirscanner
from threading import Thread
import pathlib
import socket
import sys



# Get filepath 
script_path = pathlib.Path(__file__).resolve()
script_directory = script_path.parent
FilePath = os.path.join(script_directory, "test.jpg")

# Variables to prevent race condition
# super janky, replace with locking threads
#ReceivingFile = False
fileChanged = False
activationTime = 0
Waiting = True
printing = False

# Text required for adding periods to the end as progress indicators
WaitingText = "Waiting for new file"
WaitingLength = 23
ReceivingText = "Receiving File"
ReceivingLength = 19

# Ip Address of printer
PrinterIP = "192.168.100.2"




spinner_frames = ["|", "/", "-", "\\"]

def spinner_animation(base_text, counter):
    """Prints a smooth spinner with base_text on one line"""
    frame = spinner_frames[counter % len(spinner_frames)]
    sys.stdout.write(f"\r{base_text} {frame}")
    sys.stdout.flush()

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))   # dummy connection to external host
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"  # fallback if something goes wrong

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def filescan(): #Configue directoy scanner and trigger for printer
    global Waiting, activationTime, fileChanged
    while True:
        if dirscanner.detect_file_changes(FilePath) == True:
            Waiting = False
            activationTime = time.time()
            fileChanged = True
        else:
            pass
         
def Print(): # Configure printer and activation trigger
    global fileChanged, activationTime, Waiting, printing, PrinterIP
    while True:
        time.sleep(1)
        currentTime = time.time()
        if fileChanged == True and (currentTime-activationTime) >= 3 : # Only run when the my file is changed
            printing = True
            clear_console()
            print("Preparing to print")
            printer.Print(FilePath, PrinterIP)
            activationTime = 0
            fileChanged = False
            printing = False
            Waiting = True
        else:
            pass


#Run functions as threads
thread1 = Thread(target=filescan, daemon=True)
thread2 = Thread(target=Print, daemon=True)
#Thread.start(thread1)
#Thread.start(thread2)
thread1.start()
thread2.start()

counter = 0
while True: # Simple loop to print what script is currently working on
    LocalIP = get_local_ip()

    clear_console()
    print(f"Local IP: {LocalIP}\n")  # stays at top

    if not fileChanged and Waiting:  # Waiting mode
        spinner_animation("Waiting for new file", counter)
        counter += 1
        time.sleep(0.2)

    elif fileChanged and not printing:  # Receiving mode
        spinner_animation("Receiving new file", counter)
        counter += 1
        time.sleep(0.2)

    




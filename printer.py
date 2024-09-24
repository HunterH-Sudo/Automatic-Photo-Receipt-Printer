from escpos import *
from PIL import Image
import os
import time
testing = True
PrinterIP = "192.168.100.2"


def connect():
    try:
        p = printer.Network(PrinterIP, profile="TM-T88V", timeout=3)
        return True  
    except:
        return False

connect()
    
def prnt(image):
    if connect() == True:
    
        try:
            p = printer.Network(PrinterIP, profile="TM-T88V", timeout=3)
            width, height = Image.open(image).size
            if height < width:
                image = Image.open(image).rotate(90,expand=True)
                width, height = image.size
            else:
                image = Image.open(image)
                width, height = image.size
            image.thumbnail((512,height))
            #p.image(image)
            #p.cut()
            
        except:
            print("Connected but can't print")
    else:
        print("Printer not connected")
        time.sleep(3)
    image.save(r"C:\SMB\test-mod.jpg")

def PrntNoFail(image):
    width, height = Image.open(image).size
    if height < width:
        image = Image.open(image).rotate(-90,expand=True)
        width, height = image.size
    else:
        image = Image.open(image).rotate(-90)
        width, height = image.size
    image.thumbnail((512,height))
    image.save(r"C:\SMB\test-mod.jpg")
    time.sleep(3)
    



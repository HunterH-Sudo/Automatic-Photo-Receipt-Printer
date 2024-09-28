from escpos import *
from PIL import Image
import os
import time
testing = True
PrinterIP = "192.168.100.2"

def Print(image):
    try:
        print("Trying to connect to: " + PrinterIP)
        p = printer.Network(PrinterIP, profile="TM-T88V", timeout=3)
    except:
        print("Couldn't connect to printer")
        time.sleep(3)
        return
    width, height = Image.open(image).size
    if height < width:
        image = Image.open(image).rotate(90,expand=True)
        width, height = image.size
    else:
        image = Image.open(image)
        width, height = image.size

    image.thumbnail((512,height))
    p.image(image,impl="grahics")
    p.cut()
    p.close()





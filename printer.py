from escpos import *
from PIL import Image
import os
import time
testing = True
PrinterIP = "192.168.100.2"

def Print(image):
    p = printer.Network(PrinterIP, profile="TM-T88V", timeout=10)
    width, height = Image.open(image).size
    if height < width:
        image = Image.open(image).rotate(90,expand=True)
        width, height = image.size
    else:
        image = Image.open(image)
        width, height = image.size

    image.thumbnail((512,height))
    p.image(image)
    p.cut()
    p.close()





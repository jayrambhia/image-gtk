from SimpleCV import *
from imagegtk import *

def camtest():
    cam = Camera()
    d = DisplayImage()
    while not d.isDone():
        i = cam.getImage()
        image = i.toRGB().getBitmap()
        d.show(image)
        time.sleep(0.1)
    
camtest()

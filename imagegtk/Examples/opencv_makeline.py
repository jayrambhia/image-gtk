from cv2.cv import *
from imagegtk import *
p1 = None
p2 = None

def imagetest():
    im = LoadImage("/home/jay/github-logo.png")
    image = CreateImage((im.width,im.height),im.depth,im.channels)
    CvtColor(im,image,CV_BGR2RGB)
    display = DisplayImage()
    display.image_box.connect("button_press_event",makeline,image,display)
    display.show(image)

def makeline(self,widget,image,display,data=None):
    global p1
    global p2
    print p1,p2
    if p1 is None and p2 is None:
        p1 = (display.mouseX,display.mouseY)
    elif p2 is None:
        p2 = (display.mouseX,display.mouseY)
        Line(image,p1,p2,(255,0,0),3,8)
        p1 = None
        p2 = None
        display.show(image)

imagetest()

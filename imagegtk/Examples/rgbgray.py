from imagegtk import *
from SimpleCV import *

def do_gray(widget,d,i,data=None):
    d.show(i.toGray().getBitmap())

def do_RGB(widget,d,i,data=None):
    d.show(i.toRGB().getBitmap())
    
def imagetest():
    i = Image("lenna")
    d = DisplayImage()
    
    label = gtk.Label("Lenna")
    d.box.pack_start(label,False,False,2)
    
    but1 = gtk.Button("quit")
    but1.connect("clicked",d.leave_app)
    d.box.pack_end(but1,False,False,2)
    
    but2 = gtk.Button("gray")
    d.box.pack_start(but2,False,False,2)
    but2.connect("clicked",do_gray,d,i)
    
    but3 = gtk.Button("RGB")
    d.box.pack_start(but3,False,False,2)
    but3.connect("clicked",do_RGB,d,i)
    
    d.show(i.toRGB().getBitmap())

imagetest()


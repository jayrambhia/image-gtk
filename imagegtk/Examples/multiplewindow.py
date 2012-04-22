from imagegtk import *
from SimpleCV import *

def do_gray(widget,d,i,data=None):
    d.show(i.toGray().getBitmap())

def do_RGB(widget,d,i,data=None):
    d.show(i.toRGB().getBitmap())
    
def do_HSV(widget,D,i,data=None):
    D.show(i.toHSV().getBitmap())
    
def do_BGR(widget,D,i,data=None):
    D.show(i.toBGR().getBitmap())
    
def imagetest():
    i = Image("lenna")
    d = DisplayImage()
    D = DisplayImage()
    
    label = gtk.Label("Lenna")
    d.box.pack_start(label,False,False,2)
    label = gtk.Label("Lenna")
    D.box.pack_start(label,False,False,2)
    
    but1 = gtk.Button("quit")
    but1.connect("clicked",d.leave_app)
    d.box.pack_end(but1,False,False,2)
    
    but2 = gtk.Button("gray")
    d.box.pack_start(but2,False,False,2)
    but2.connect("clicked",do_gray,d,i)
    
    but3 = gtk.Button("RGB")
    d.box.pack_start(but3,False,False,2)
    but3.connect("clicked",do_RGB,d,i)
    
    but5 = gtk.Button("HSV")
    D.box.pack_start(but5,False,False,2)
    but5.connect("clicked",do_HSV,D,i)
    
    but4 = gtk.Button("BGR")
    D.box.pack_start(but4,False,False,2)
    but4.connect("clicked",do_BGR,D,i)
    
    but5 = gtk.Button("quit")
    but5.connect("clicked",D.leave_app)
    D.box.pack_end(but5,False,False,2)
    
    d.show(i.toRGB().getBitmap())
    D.show(i.toRGB().getBitmap())

imagetest()


from pygtk_image import *
from SimpleCV import *

def do_done(widget,d,data=None):
    d.done = True
    time.sleep(d.interval+0.05)
    
def imagetest():
    i = Image("lenna")
    d = DisplayImage()
    label = gtk.Label("Lenna")
    d.box.pack_start(label,False,False,2)
    but1 = gtk.Button("quit")
    but1.connect("clicked",d.leave_app)
    d.box.pack_start(but1,False,False,2)
    but2 = gtk.Button("done")
    d.box.pack_start(but2,False,False,2)
    but2.connect("clicked",do_done,d)
    d.show_image(i.toRGB().getBitmap())
    d.show_image(i.toGray().getBitmap())

imagetest()


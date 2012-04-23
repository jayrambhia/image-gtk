from SimpleCV import *
from imagegtk import DisplayImage

def change_size(widget,d,i):
    width = d.entry1.get_text()
    height = d.entry2.get_text()
    if width and height:
        width = int(width)
        height = int(height)
        print width, height
        if width <= 512 and height <= 512:
            d.set_image_size((width,height))

def sizetest():
    #im = Image("lenna")
    #image = im.toRGB().getBitmap()
    image = "python-logo.png"
    d = DisplayImage(winsize=(800,600),imgsize=(320,240),title="sizetest")
    
    d.hbox1 = gtk.HBox(False,2)
    d.box.pack_start(d.hbox1,False,False,2)
    d.label1 = gtk.Label("width")
    d.hbox1.pack_start(d.label1,False,False,2)
    d.entry1 = gtk.Entry()
    d.hbox1.pack_start(d.entry1,False,False,0)
    
    d.hbox2 = gtk.HBox(False,2)
    d.box.pack_start(d.hbox2,False,False,2)
    d.label2 = gtk.Label("height")
    d.hbox2.pack_start(d.label2,False,False,2)
    d.entry2 = gtk.Entry()
    d.hbox2.pack_start(d.entry2,False,False,0)
    
    d.but1 = gtk.Button("set size")
    d.but1.connect("clicked",change_size,d,image)
    d.but1.set_size_request(100,30)
    d.box.pack_end(d.but1,False,False,2)
    
    d.show(image)
    
sizetest()

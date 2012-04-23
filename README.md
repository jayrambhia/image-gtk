#imagegtk
###Author: Jay Rambhia


A library to build a gtk GUI around an image. An easy way to show multiple images simultaneously with customizable GUI.
Mainly built for the purpose to show images in OpenCV or SimpleCV with customizable GUI.

##[wiki] (https://github.com/jayrambhia/image-gtk/wiki/imagegtk)
##[docs](https://github.com/jayrambhia/image-gtk/wiki/docs)

####Examples:
#####1. From file
    
    image = "python-logo.png"
    d = DisplayImage()
    d.show(image)
    
#####2. OpenCV

    im = LoadImage(filename)
    image = CreateImage((im.width,im.height),im.depth,im.channels)
    CvtColor(im,image.CV_BGR2RGB)

    d = DisplayImage(title="iamgegtk")
    
    label = gtk.Label("Lenna")
    d.box.pack_start(label,False,False,0)
    
    but1 = gtk.Button("Quit")
    but1.connect("clicked",d.leave_app)
    d.box.pack_end(but1,False,False,2)
    
    d.show(image)
    
#####3. SimpleCV

    im = Image("Lenna")
    image = im.toRGB.getBitmap()
    
    d = DisplayImage(title="iamgegtk")
    
    label = gtk.Label("Lenna")
    d.box.pack_start(label,False,False,0)
    
    but1 = gtk.Button("Quit")
    but1.connect("clicked",d.leave_app)
    d.box.pack_end(but1,False,False,2)
    
    d.show(image)
    



import gtk
from threading import Thread
import gobject
import time
gtk.gdk.threads_init()

class DisplayImage():
    def __init__(self,winsize=None,imgsize=None,title="imagegtk"):
        """
        Constructs gtk window and adds widgets
        parameters:
            title - A string for window title
        """
        self.img = None
        self.img_gtk = None
        self.img_thrd = None
        self.img_thrd_flag = False
        self.interval = 0.1
        self.mouseX = 0
        self.mouseY = 0
        self.mouse_rawX = 0
        self.mouse_rawY = 0
        self.done = False
        self.thrd = None
        self.mouseLeft = 0
        self.mouseRight = 0
        self.mouseMiddle = 0
        self.leftButtonDown = 0
        self.rightButtonDown = 0
        self.winsize = winsize
        self.imgsize = imgsize
        
        self.win = gtk.Window()
        self.win.set_title(title)
        if self.winsize is not None:
            self.win.set_size_request(self.winsize[0],self.winsize[1])
        self.win.connect("delete_event",self.leave_app)
        self.box = gtk.VBox(False,2)
        self.win.add(self.box)
        self.box.show()
        self.image_box = gtk.EventBox()
        self.image_box.connect("motion_notify_event",self.motion_callback)
        self.image_box.connect("button_press_event",self.press_callback)
        self.image_box.connect("button_release_event",self.release_callback)
        self.box.pack_start(self.image_box,False,False,2)
        
    def show(self,image,imgsize=None):
        """
        Summary:
            Creates a thread to show image and calls show_image
            
        Parameters:
            image - cv2.cv.iplimage or iplimage
        """
        if imgsize is not None and type(imgsize) is tuple:
            self.imgsize = imgsize
        if self.img_thrd:
            # Thread exists. Hence change the flag to end the thread.
            self.img_thrd_flag = False
        self.img_thrd = Thread(target = self.__showimage,args=(image,),name="show_image")
        self.img_thrd.start()
    
    def __showimage(self,image):
        """
        Summary:
            Creates pixbuf from image data. Sets image from pixbuf.
            Creates a thread to call gtk.main()
            
        Parameters:
            image - cv2.cv.iplimage or iplimage
            
        NOTE:
            This function shouldn't be called directly
        """
        if self.done == True and self.img_gtk is None:
            self.done = False
            self.__init__()
        elif self.done == True:
            self.done = False
            
        self.img = image
        self.img_thrd_flag = True
        
        if self.img_gtk is None:
            self.img_flag=0
            self.img_gtk = gtk.Image()
            self.image_box.add(self.img_gtk)
        
        if type(self.img) == str:
            self.img_pixbuf = gtk.gdk.pixbuf_new_from_file(self.img)
        else:
            self.img_pixbuf = gtk.gdk.pixbuf_new_from_data(self.img.tostring(),
                                                        gtk.gdk.COLORSPACE_RGB,
                                                        False,
                                                        self.img.depth,
                                                        self.img.width,
                                                        self.img.height,
                                                        self.img.width*self.img.nChannels)
        if self.imgsize is not None:
            self.img_pixbuf = self.__resizeImage(self.img_pixbuf,self.imgsize)
            
        self.img_gtk.set_from_pixbuf(self.img_pixbuf)
        self.img_gtk.show()
        self.win.show_all()
        
        if not self.img_flag:
            self.__threadgtk()
            self.img_flag=1                     
            
        while (not self.done and self.img_thrd_flag) :
            time.sleep(self.interval/2)
    
    def __threadgtk(self):
        """
        Summary:
            Creates a thread for gtk.main()
        """
        self.thrd = Thread(target=gtk.main, name = "GTK thread")
        self.thrd.daemon = True
        self.thrd.start()
    
    def leave_app(self,widget,data=None):
        """
        Summary:
            calls quit.
        Note:
            This function must be called with a callback.
        """
        self.quit()
    
    def release_callback(self,widget,event):
        """
        Callback function when mouse button is released.
        Updates mouseX, mouseY, mouse_rawX, mouse_rawY
        """
        self.mouseX = int(event.x)
        self.mouseY = int(event.y)
        self.mouse_rawX = int(event.x_root)
        self.mouse_rawY = int(event.y_root)
        self.setReleaseButtonState(event.button)
    
    def press_callback(self,widget,event):
        """
        Callback function when mouse button is pressed.
        Updates mouseX, mouseY, mouse_rawX, mouse_rawY
        """
        self.mouseX = int(event.x)
        self.mouseY = int(event.y)
        self.mouse_rawX = int(event.x_root)
        self.mouse_rawY = int(event.y_root)
        self.setPressButtonState(event.button)
        
    def setPressButtonState(self, mode):
        if mode == 1:
            self.leftButtonDown = 1
            self.mouseLeft = 1
        elif mode == 2:
            self.rightButtonDown = 1
            self.mouseLeft = 1
        elif mode == 3:
            self.mouseMiddle = 1
            
    def setReleaseButtonState(self, mode):
        if mode == 1:
            self.leftButtonDown = 0
            self.mouseLeft = 0
        elif mode == 2:
            self.rightButtonDown = 0
            self.mouseLeft = 0
        elif mode == 3:
            self.mouseMiddle = 0
        
    def motion_callback(self,widget,event):
        """
        Callback function when mouse is moved.
        Updates mouseX, mouseY, mouse_rawX, mouse_rawY
        """
        self.mouseX = int(event.x)
        self.mouseY = int(event.y)
        self.mouse_rawX = int(event.x_root)
        self.mouse_rawY = int(event.y_root)
    
    def isDone(self):
        """
        Check whether window exists or not
        """
        return self.done
    
    def quit(self):
        """
        Destroys window, image.
        """
        self.img_gtk = None
        self.win.destroy()
        self.done = True
        
    def change_title(self,title=None):
        """
        Change the title of the window.
        Parameter:
            title - A string
        
        Changes the title of the window
        
        Example:
            d = DisplayImage(title="imagegtk")
            d.change_title("my title")
        """
        if title is not None:
            self.win.set_title(title)
            self.win.show_all()
    
    def change_size(self,size):
        """
        Change the size of the window.
        Parameter:
            size - a tuple containing 2 integers
        
        Changes the size of the window
        
        Example:
            d = DisplayImage(size=(800,600))
            d.change_size((400,300))
        """
        if size:
            self.win_size = size
            self.win.set_size_request(self.win_size[0], self.win_size[1])
            self.win.show_all()
    
    def __resizeImage(self,pixbuf,size):
        """
        Parameters:
            pixbuf - gtk.gdk.pixbuf
            size - a tuple containing 2 integers
            
        Returns resized gtk.gdk.pixbuf
        """
        new_pixbuf = pixbuf.scale_simple(size[0],size[1],gtk.gdk.INTERP_BILINEAR)
        return new_pixbuf
    
    def set_image_size(self,size):
        """
        To set or change the size of the image.
        
        Parameters:
            size - A tuple of two integers
            
        Example:
            display = DisplayImage()
            i = Image("lenna")
            display.show(i.toRGB().getBitmap)
            display.set_image_size((400,300))
            ===============================================================
            
            im = LoadImage("filename.jpg")
            image = CreateImage((im.width,im.height),im.depth,im.channels)
            CvtColor(im,image,CV_BGR2RGB)
            display = DisplayImage()
            display.show(image)
            display.set_image_size((400,300))
            ===============================================================
        """
        #http://faq.pygtk.org/index.py?req=show&file=faq08.006.htp
        if size:
            # Need to add more something to choose for interp_type
            # current interp_type = gtk.gdk.INTERP_BILINEAR
            # http://www.pygtk.org/docs/pygtk/class-gdkpixbuf.html#method-gdkpixbuf--scale-simple
            # Should I change the original pixbuf or not ?
            #new_buf = self.img_pixbuf.scale_simple(size[0],size[1],gtk.gdk.INTERP_BILINEAR)
            new_buf = self.__resizeImage(self.img_pixbuf,size)
            self.imgsize = size
            self.img_gtk.set_from_pixbuf(new_buf)
            self.img_gtk.show()
            

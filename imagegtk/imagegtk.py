import gtk
from threading import Thread
import gobject
import time
gtk.gdk.threads_init()

class DisplayImage():
    def __init__(self,title="SimpleCV"):
        self.img = None
        self.img_gtk = None
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
        self.win = gtk.Window()
        self.win.set_title(title)
        self.win.connect("delete_event",self.leave_app)
        self.box = gtk.VBox(False,2)
        self.win.add(self.box)
        self.box.show()
        self.image_box = gtk.EventBox()
        self.image_box.connect("motion_notify_event",self.motion_callback)
        self.image_box.connect("button_press_event",self.press_callback)
        self.image_box.connect("button_release_event",self.release_callback)
        self.box.pack_start(self.image_box,False,False,2)
    
    def show_image(self,image):
        if self.done == True and self.img_gtk is None:
            self.done = False
            self.__init__()
        elif self.done == True:
            self.done = False
        self.img = image
        if self.img_gtk is None:
            self.img_flag=0
            self.img_gtk = gtk.Image()          # Create gtk.Image() only once (first time)
            print self.img_gtk
            self.image_box.add(self.img_gtk)    # Add Image in the box, only once (first time)
            
        self.img_pixbuf = gtk.gdk.pixbuf_new_from_data(self.img.tostring(),
                                                        gtk.gdk.COLORSPACE_RGB,
                                                        False,
                                                        self.img.depth,
                                                        self.img.width,
                                                        self.img.height,
                                                        self.img.width*self.img.nChannels)
        self.img_gtk.set_from_pixbuf(self.img_pixbuf)
        self.img_gtk.show()
        self.win.show_all()
        if not self.img_flag:
            self.thread_gtk()                   # gtk.main() only once (first time)
            self.img_flag=1                     # change flag
        while not self.isDone():
            time.sleep(self.interval)
    
    def remove_image(self):
        self.image_gtk = None
    
    def thread_gtk(self):
        # changed this function. Improved threading.
        self.thrd = Thread(target=gtk.main, name = "GTK thread")
        self.thrd.daemon = True
        self.thrd.start()
    
    def leave_app(self,widget,data=None):
        #self.done = True
        #self.win.destroy()
        #gtk.main_quit()
        self.quit()
    
    def release_callback(self,widget,event):
        self.mouseX = int(event.x)
        self.mouseY = int(event.y)
        self.mouse_rawX = int(event.x_root)
        self.mouse_rawY = int(event.y_root)
        self.setReleaseButtonState(event.button)
        #print self.mouseX, self.mouseY, self.mouse_rawX, self.mouse_rawY,"leave"
    
    def press_callback(self,widget,event):
        self.mouseX = int(event.x)
        self.mouseY = int(event.y)
        self.mouse_rawX = int(event.x_root)
        self.mouse_rawY = int(event.y_root)
        self.setPressButtonState(event.button)
        #print self.mouseX, self.mouseY, self.mouse_rawX, self.mouse_rawY,"press"
        
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
        self.mouseX = int(event.x)
        self.mouseY = int(event.y)
        self.mouse_rawX = int(event.x_root)
        self.mouse_rawY = int(event.y_root)
        #print self.mouseX, self.mouseY, self.mouse_rawX, self.mouse_rawY,"motion"
    
    def isDone(self):
        return self.done
    
    def quit(self):
        self.done = True
        self.img_gtk = None
        self.win.destroy()
        gtk.main_quit()

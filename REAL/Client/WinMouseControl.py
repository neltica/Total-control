from pymouse import PyMouse

class WinMouseControl():
    
    mouseObject=''
    def __init__(self):
        self.mouseObject=PyMouse()
        print "mouse init success"
        pass
    
    def __del__(self):
        pass
    
    def mouseMove(self,x,y,button=None):
        self.mouseObject.move(x, y)
        return 0
    
    def mouseClick(self,x,y,button):
        self.mouseObject.click(x, y, button)   #button:1 left, button2: middle button3:right
        return 0
    
    def mousePress(self,x,y,button):
        self.mouseObject.press(x, y, button)   #button:1 left, button2: middle button3:right
        return 0
    
    def mouseRelease(self,x,y,button):
        self.mouseObject.release(x, y, button)   #button:1 left, button2: middle button3:right
        return 0
    
if __name__=="__main__":
    mouse=WinMouseControl()
    mouse.mouseMove(10,10,1)
    mouse.mousePress(10,10,1)
    mouse.mouseRelease(10,10,1)
    pass

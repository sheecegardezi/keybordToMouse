import keyboard, mouse, time

class keyboardToMouseApp:
    def __init__(self, HOULD_TIME = 2):
        self.HOULD_TIME = HOULD_TIME
        self.run = True
        
    def main(self):
        self.intro()
        self.lister = keyboard.hook(self.filter_key)
        while self.run:
            pass
        
    def intro(self):
        print("Mouse Control App")
        print("Simulate mouse press wen key is down")
        print("Hit 'z' to simulate left mouse press and hold for ", self.HOULD_TIME)
        print("Hit 'x' to simulate right mouse press and hold for ", self.HOULD_TIME)
        print("Hit 'c' to simulate center mouse press and hold for ", self.HOULD_TIME)
        print("Hit 'v' to simulate right mouse click ", self.HOULD_TIME)
        print("Hit 'esc' to terminate app ")

    def mouseUp(self, MBUTTON):
        mouse.release(MBUTTON)

    def mouseDown(self, MBUTTON):
        mouse.press(MBUTTON)

    def filter_key(self, event):
        if event.name == 'z' and event.event_type == 'up': 
            print (event.name, event.event_type)
             
            print ('left mouse is down')
            mouse.press(mouse.LEFT)
            
            time.sleep(self.HOULD_TIME)

            print ('left mouse is up')
            mouse.release(mouse.LEFT)

        elif event.name == 'x' and event.event_type == 'up': 
            print (event.name, event.event_type, event.time)
            
            print ('right mouse is down')
            mouse.press(mouse.RIGHT)
            
            # sleep for some time
            time.sleep(self.HOULD_TIME)

            print ('right mouse is up')
            mouse.release(mouse.RIGHT)

        elif event.name == 'v' and event.event_type == 'up': 
            print (event.name, event.event_type, event.time)
            
            print ('right mouse is click')
            mouse.click(mouse.RIGHT)
            
        elif event.name == 'c' and event.event_type == 'up': 
            print (event.name, event.event_type)
            
            print ('middle mouse is down')
            mouse.press(mouse.MIDDLE)
            
            # sleep for some time
            # time.sleep(self.HOULD_TIME)

            print ('midle mouse is up')
            mouse.release(mouse.MIDDLE)
            
        elif event.name == 'u' and event.event_type == 'up': 
            print (event.name, event.event_type)
            
            print ('scroll mouse wheel up')
            mouse.wheel(1)
                        
        elif event.name == 'j' and event.event_type == 'up': 
            print (event.name, event.event_type)
            
            print ('scroll mouse wheel down')
            mouse.wheel(-1)
                        
            
        elif event.name == 'esc' and event.event_type == 'up': 
            print (event.name, event.event_type)
            # exit
            keyboard.wait()
            self.run = False
            
            print ('esc key is down exiting')

if __name__ == "__main__":
    #help(keyboard)
    App = keyboardToMouseApp()
    App.main()


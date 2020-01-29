from pynput.mouse import Listener
from pynput.mouse import Button, Controller
import time
mouse = Controller()
##f=open("mouse_log.txt", "w+")
f=open("mouse_log.txt", "r")
lines = f.readlines()
f.close()

for line in lines:
    line = line.strip("Mouse moved to (").replace(')','')
    if(not("clicked" in line)):
        print( line.split(',')[0] )
        time.sleep(0.01)
        mouse.position = (int(line.split(',')[0]), int(line.split(',')[1]))
        
    else:
        x = line.split('(')[1].replace('with Button.left','').split(',')[0]
        y = line.split('(')[1].replace('with Button.left','').split(',')[1]
        print(line.split('with ')[1] + " " + line.split('(')[1].replace('with Button.left','').split(',')[0])
        mouse.position = (int(x), int(y))        
        mouse.click(Button.left, 1)


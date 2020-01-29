from pynput.mouse import Listener
f=open("mouse_log.txt", "w+")
##from pynput.mouse import Button, Controller
##import logging
##
##logging.basicConfig(filename=("recorded_mouse.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
##mouse = Controller()
##
##def on_move(x,y):
##    ##print(x, y)
##    ##print("Mouse moved to ({0}, {1})".format(x,y))
##    logging.info(x,y)
##    
##def on_click(x,y,dx,dy):
##    ##print(x, y, dx, dy)
##    logging.info(x,y, dx, dy)
##    
##def on_scroll(x,y,dx,dy):
##    ##print(x, y, dx, dy)
##    logging.info(x,y, dx, dy)
##    
##with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
##    listener.join()

def on_move(x, y):
    ##f.write("Test {0}, {1}\r\n".format(x, y))
    ##logging.info("Mouse moved to ({0}, {1})".format(x, y))
    ##f.write("Mouse moved to ({0}, {1})\r\n".format(x, y))
    f.write("Mouse moved to ({0}, {1})\r\n".format(x, y))
    
def on_click(x, y, button, pressed):
    if pressed:
        ##logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        f.write('Mouse clicked at ({0}, {1}) with {2}\r\n'.format(x, y, button))
        
def on_scroll(x, y, dx, dy):
    ##logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
    f.write('Mouse scrolled at ({0}, {1})({2}, {3})\r\n'.format(x, y, dx, dy))
    
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
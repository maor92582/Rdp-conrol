import socket
from pynput import mouse
import time
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.155",65155))
done=False
def se(x,y,button,pressed):
    if(pressed):
        tb=str(button).split(".")[1]
        print(tb)
        s.send(tb.encode())
li=mouse.Listener(on_click=se)
li.start()
li.join()
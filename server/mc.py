import socket
from pynput import mouse
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
other_ip = "127.0.0.1"
port=65155
s.connect((other_ip,port))
done=False
def se(x,y,button,pressed):
    if(pressed):
        tb=str(button).split(".")[1]
        print(tb)
        s.send(tb.encode())
li=mouse.Listener(on_click=se)
li.start()
li.join()
import pyautogui
import socket
import struct
import time
def func():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.155",65255))
    while True:
        try:
            x=pyautogui.position()
            size=int(len(str(x.x)+":"+str(x.y)))
            print(size)
            size=struct.pack('!I', size)
            s.send(size)
            print((str(x.x)+":"+str(x.y)))
            s.sendall((str(x.x)+":"+str(x.y)).encode())
            time.sleep(1.5)
        except:
            func()
func()        

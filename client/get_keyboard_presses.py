import keyboard
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=65514
s.bind(('0.0.0.0',port))
s.listen()     
c, addr=s.accept()
print(addr)
while True:
    key=c.recv(1)
    print(key.decode())
    keyboard.press(''.join(key.decode()))
    keyboard.release(''.join(key.decode()))

    
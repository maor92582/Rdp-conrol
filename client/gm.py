import pyautogui
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=65510
s.bind(('0.0.0.0',port))
s.listen()
c,ip=s.accept()
print(ip)
while True:
    x= c.recv(1024).decode()
    x=x.split(":")
    print(x)
    pyautogui.moveTo(int(x[0]),int(x[1]),duration=1)



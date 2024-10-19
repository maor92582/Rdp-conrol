import socket
import os
import time
from filelock import FileLock
lock_path = r"C:\Users\maori\Documents\Rdp\locks\attacker.lock"
filedata=b''
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0',65534))
os.chdir(r"C:\Users\maori\Documents\Rdp\server\ImgTO")
done=False
def Get():
    global done
    global filedata
    while done==False:
        file=s.recvfrom(100)                
        if(file[0]==b"<end>"):
            done=True
        else:
            filedata+=file[0]
    with open("screenshot.png",'wb') as filec:
        filec.write(filedata)
    filedata=b''
    done=False
while True:
    with FileLock(lock_path):
        Get()
    time.sleep(0.1)




        
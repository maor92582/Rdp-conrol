import socket
import os
import time
from filelock import FileLock
lock_path = r"C:\Users\maori\Documents\Rdp\locks\client.lock"

global name1
name1="temp.jpg"
other_ip = "192.168.1.155"
port=65534
ct=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort   = (other_ip, port)
chunk_size=100
def openfile():
    global filepath
    filepath=r"C:\Users\maori\Documents\Rdp\client\images\screenshot.png"  
    with open(filepath, 'rb') as file:
        data = file.read()
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    for chunk_index, x in enumerate(chunks):
        ct.sendto(x, serverAddressPort)
    ct.sendto(b"<end>", serverAddressPort)    
    print("File sent successfully")
while True:
    with FileLock(lock_path):
        openfile()
    time.sleep(0.1)

ct.close()
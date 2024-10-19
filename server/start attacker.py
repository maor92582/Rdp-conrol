import os
import threading
data_lock=threading.Lock()
from filelock import FileLock
import time

def app():
    while True:
        try:
            os.system('python C:\\Users\\maori\\Documents\\Rdp\\server\\app.py')
            
        except:
            time.sleep(2)


def server():
    while True:
        try:
            os.system('python C:\\Users\\maori\\Documents\\Rdp\\server\\server.py')
            print(1)
        except:
            time.sleep(2)
def kb():
    while True:
        try:
            os.system('python C:\\Users\\maori\\Documents\\Rdp\\server\\kbs.py')
        except:
            time.sleep(2)

def mouse():
    while True:
        try:
            os.system('python C:\\Users\\maori\\Documents\\Rdp\\server\\sm.py')
        except:
            time.sleep(2)
def mousec():
    while True:
        try:
            os.system('python C:\\Users\\maori\\Documents\\Rdp\\server\\mc.py')
        except:
            time.sleep(2)
# יצירת תהליכים מבלי להריץ אותם מיד
t1 = threading.Thread(target=app)  # תהליך ראשון
t2 = threading.Thread(target=server)  # תהליך שני
t3 = threading.Thread(target=kb)  # תהליך שני
t4 = threading.Thread(target=mouse)  # תהליך שני
t5 = threading.Thread(target=mousec)  # תהליך שני

# הפעלת התהליכים
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# חכות עד שהשניים יסיימו
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

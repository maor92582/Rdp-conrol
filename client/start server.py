import os
import threading
import time
def pg():
    try:
        os.system('python C:\\Users\\maori\\Documents\\Rdp\\client\\pg.py')
    except:
        time.sleep(2)
        pg()

def client():
    try:
        os.system('python C:\\Users\\maori\\Documents\\Rdp\\client\\client.py')
    except:
        time.sleep(2)
        client()
def kb():
    try:
        os.system('python C:\\Users\\maori\\Documents\\Rdp\\client\\kbg.py')
    except:
        time.sleep(2)
        kb()
def mouse():
    try:
        os.system('python C:\\Users\\maori\\Documents\\Rdp\\client\\gm.py')
    except:
        time.sleep(2)
        mouse()
# יצירת תהליכים מבלי להריץ אותם מיד
t1 = threading.Thread(target=pg)  # תהליך ראשון
t2 = threading.Thread(target=client)  # תהליך שני
t3 = threading.Thread(target=kb)  # תהליך שני
t4 = threading.Thread(target=mouse)  # תהליך שני

# הפעלת התהליכים
t1.start()
t2.start()
t3.start()
t4.start()

# חכות עד שהשניים יסיימו
t1.join()
t2.join()
t3.join()
t4.join()

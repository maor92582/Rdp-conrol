import os
import threading
import time
def get_mouse_clicks():
    try:
        os.system('python C:\\Users\\maori\\Documents\\Rdp\\client\\get_mouse_clicks.py')
    except:
        time.sleep(2)
        get_mouse_clicks()

def client():
    try:
        os.system('python C:\\Users\\maori\\Documents\\Rdp\\client\\client.py')
    except:
        time.sleep(2)
        client()
def kb():
    try:
        os.system('python C:\\Users\\maori\\Documents\\Rdp\\client\\get_keyboard_presses.py')
    except:
        time.sleep(2)
        kb()
def mouse():
    try:
        os.system('python C:\\Users\\maori\\Documents\\Rdp\\client\\get_mouse_postion.py')
    except:
        time.sleep(2)
        mouse()
# יצירת תהליכים מבלי להריץ אותם מיד
t1 = threading.Thread(target=get_mouse_clicks)  # תהליך ראשון
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

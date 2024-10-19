import pyautogui
import time
from PIL import Image
from filelock import FileLock
lock_path = r"C:\Users\maori\Documents\Rdp\locks\client.lock"


def Is():
    print("__________start__________")
    screen=pyautogui.screenshot()
    screen.save(r"C:\\Users\\maori\\Documents\\Rdp\\client\\images\\tenm.png")   
    foo = Image.open(r"C:\\Users\\maori\\Documents\\Rdp\\client\\images\\tenm.png")
    print(foo.size)
    foo = foo.resize((640,480),Image.ANTIALIAS)
    foo.save(r"C:\\Users\\maori\\Documents\\Rdp\\client\\images\\screenshot.png", optimize=True, quality=95)
while True:
    with FileLock(lock_path):
        Is()
    time.sleep(0.05)

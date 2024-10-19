import socket
import threading
import time
import tkinter
from PIL import ImageTk, Image,ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
frame=tkinter.Tk()
frame.tkraise()
from filelock import FileLock
lock_path = r"C:\Users\maori\Documents\Rdp\locks\attacker.lock"
frame.attributes('-fullscreen',True)
def load_image():
    try:               
        img = Image.open(r"C:\Users\maori\Documents\Rdp\server\ImgTO\screenshot.png")
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
def update_image():
    # טעינת התמונה מחדש
    img = load_image()
    if img:
        label1.config(image=img)
        label1.image = img
        print("update")
    else:
        label1.config(text="Failed to load image")
    with FileLock(lock_path):
        frame.after(200, update_image)
        

img=load_image()
if img:
    label1 = tkinter.Label(frame,image=img)
    label1.pack()
    

with FileLock(lock_path):
    frame.after(200, update_image)
        


frame.mainloop()


        
        


        

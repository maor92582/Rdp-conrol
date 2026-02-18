from pynput.mouse import Button, Controller
import socket
mouse=Controller()
def get_mouse_clicks():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port=65155
    s.bind(('0.0.0.0',port))
    s.listen()  
    c,ip=s.accept()
    print(ip)
    while True:
        x=c.recv(1024).decode()
        if(x=="left"):
            mouse.press(Button.left)
            print("left")
        elif(x=="right"):
            mouse.press(Button.right)
            print("right")
        elif(x=="middle"):
            mouse.press(Button.middle)
            print("middle")
        else:
            print("error:{x}")
get_mouse_clicks()        

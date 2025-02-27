from tkinter import *
import os 

root=Tk()
root.title("Shutdown App")
root.geometry("400x580")

def restarttime():
    os.system("shutdown /r /t 30")

def restart():
    os.system("shutdown /r /t 1")

def shutdown():
    os.system("shutdown /s /t 1")

def logout():
    os.system("shutdown /l")


image_restart=PhotoImage(file="restart time.png")
btn1=Button(root,image=image_restart,borderwidth=0,cursor="hand2",command=restarttime)
btn1.place(x=10,y=10)

image_close=PhotoImage(file="close (1).png")
btn2=Button(root,image=image_close,borderwidth=0,cursor="hand2",command=root.destroy)
btn2.place(x=200,y=10)

image_rest=PhotoImage(file="restart.png",)
btn3=Button(root,image=image_rest,borderwidth=0,cursor="hand2",command=restart)
btn3.place(x=10,y=200)

image_shutdown=PhotoImage(file="shutdown.png")
btn4=Button(root,image=image_shutdown,borderwidth=0,cursor="hand2",command=shutdown)
btn4.place(x=200,y=200)

image_logout=PhotoImage(file="log out.png")
btn5=Button(root,image=image_logout,borderwidth=0,cursor="hand2",command=logout)
btn5.place(x=10,y=400)

root.mainloop()

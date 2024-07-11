#wapp to generate random motivational msg
from tkinter import *
from requests import *
root=Tk()
root.title("App by KS")
root.geometry("1200x600+50+50")
root.configure(bg="lightgreen")
f=("Arial",40,"bold")

def msg():
    wa="https://api.quotable.io/random"
    res=get(wa)
    data=res.json()
    msg=data["content"]
    lab.configure[text=msg]
    root.after(3000,message)



    

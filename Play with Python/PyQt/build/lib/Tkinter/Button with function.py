from tkinter import *
root = Tk()
root.geometry("1000x500+50+50")

def show():
        n = ent.get()
        msg = "Welcome "+ n + " ! \n How are you ? "
        ans.configure(text = msg)

f = ("Times New Roman",30,"bold")

lab = Label( root, text = " \n Enter Your Name", font = f )
ent = Entry( root, font = f )
btn = Button( root, text = "Click me", font = f, bg = "lightblue", command = show )
ans = Label( root, font = f ) 

lab.pack()
ent.pack()
btn.pack()
ans.pack()
root.mainloop()






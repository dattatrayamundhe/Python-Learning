from tkinter import *
root = Tk()
root.geometry("1000x500")
root.configure(bg = "lightblue")

f=("Arial",12,"bold")

lab = Label(root, text ="What is the syntax of label in tkinter ?",font = f, fg ="red", bg = "lightblue")
lab.pack(pady = 30)

lab1= Label(root,text ="label = label( root, text = 'our text whatever we want print' , font = ('Rockwell', 30, 'bold'), fg = 'blue', bg = 'gray' )",font= f, fg = "black",bg = "lightblue")
lab1.pack(pady = 30)

lab2 = Label( root,text = "Where are you ?",font = f, fg = "white",bg = "lightblue")
lab2.pack(pady = 30)

root.mainloop()

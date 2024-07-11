from tkinter import *
root = Tk()
root.geometry("1200x500+50+50")

f = ( "Simsun", 30, "bold" )

def find():
        try:
            radius = float(ent.get())

        except ValueError :
            ans.configure(text = "You need enter number Only ")
            return
        if radius <= 0.0:
            ans.configure(text = "Don't be Negative")
            return
        area = 3.14*radius**2
        circum = 2*3.14*radius
        area = round(area,2)
        circum = round(circum,2)
        msg = "Area = "+str(area)+" \n Circumference = "+str(circum)
        ans.configure(text = msg)

lab = Label( root,text = "Enter radius",font = f)
lab.pack()
ent = Entry( root,font = f )
ent.pack()
btn = Button( root, text = "Compute", font = f, bg = "#969", command = find )
btn.pack()
ans = Label( root, font = f )
ans.pack()

root.mainloop()





        





            

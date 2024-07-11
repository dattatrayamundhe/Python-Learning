from tkinter import *
root = Tk()
root.title("Area of rectangle")
root.geometry("1200x500+50+50")

f = ( "Arial", 30, "bold" )

def find() :
        try :
            length = float(ent.get())
        except ValueError :
                ans.configure( text = "Invalid length" )
                return
        if length <= 0.0 :
            ans.configure( text = "Negative length not allowed" )
            return
        try :
            breadth = float(ent2.get())
        except ValueError :
                ans.configure(text = "Invalid breadth")
                return
        if breadth <= 0.0 :
                ans.configure(text="Negative breadth not allowed")
                return
        area = length*breadth
        area = round(area, 2)
        msg = "Area = "+ str(area)
        ans.configure(text = msg)
            
                
            
lab = Label( root, text = "\nEnter length ", font = f )
lab.pack()
ent = Entry( root,font = f )
ent.pack()

lab2 = Label( root,text = "\nEnter breadth ", font = f)
lab2.pack()
ent2 = Entry( root,font = f )
ent2.pack()

btn = Button( root, text = "Compute", font = f, bg = "#969", command = find )
btn.pack()
ans = Label( root, font = f )
ans.pack()

root.mainloop()

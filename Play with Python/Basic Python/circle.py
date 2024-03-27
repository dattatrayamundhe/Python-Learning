#wapp to read radius from the user 
#print area and circumference of circle
#provide radius is +ve

radius = float(input("Enter the radius : "))

print("Radius is " , radius)

circumference=round(2*3.14*radius)
print(f"Circumference of circle is {circumference} units.")

area=3.14*radius**2
print(f"The area of circle is {area} units per square.")


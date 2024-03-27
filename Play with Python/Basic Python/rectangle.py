#wapp to read length and breadth 
# print area & perimeter of rectangle

len=float(input("enter the length "))
bre=float(input("enter the breadth "))

if (len>0.0) and (bre>0.0):
	area=len*bre
	perimeter=2*(len+bre)
	print("area of rectangle is" + area)
	print("Perimeter of rectangle is" +perimeter)
else:
	print("Invalid length & breadth")
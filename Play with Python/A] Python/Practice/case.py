'''
waap to read rating between 1 to 5 and print feedback
5/4 ==> Excellent
3/2 ==> Good 
1   ==> Ok

'''

r = int(input("Enter rating between 1 to 5 :\a"))

'''
if r==4 or r==5:
	print ("The rating is excellent")
elif r==2 or r==3:
	print ("The rating is Good")
elif r==1:
	print ("The rating is Ok")
else:
	print("Invalid rating")
'''


match r:
	case	5: print("Excellent ")
	case	4: print("Excellent")
	case	3: print("good")
	case	2: print("good")
	case	1: print("ok")
	case	_: print("Invalid rating")
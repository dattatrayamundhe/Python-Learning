#love calculator
name1 = input('Enter your Firstname : \n')
name2 = input("Enter his/her Firstname : \n")

combine = name1 + name2
lower_case  = combine.lower()

t = lower_case.count('t')
r = lower_case.count('r')
u = lower_case.count('u')
e = lower_case.count('e')

true = t + r + u + e

l = lower_case.count('t')
o = lower_case.count('r')
v = lower_case.count('u')
e = lower_case.count('e')

love = l + o + v + e
love_score = int(str( true) + str(love))

if ( love_score >=10 and love_score < 40 ) :
    print(f"Your love score is {love_score} which is low and you have attraction towards {name2}.")

elif ( love_score >=40 and love_score < 60 ) :
    print(f"Your love score is {love_score} which is medium and you can live in relation with {name2}.")

elif ( love_score >=60 and love_score < 100 ) :
    print(f"Your love score is {love_score} which is high and you have true love for {name2}.\n Congrats you got your first love !!!")

elif ( love_score >=1 ):
    print(f"Your love score is {love_score} which is very low so leave it !!")

else :
    print(f"Invalid input ! please give valid input.....")



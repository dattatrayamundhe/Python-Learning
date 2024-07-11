#WAP for getting prime factors of random number
import random
n=( random.randint(0,99) )
d=2
print("The prime factors of {} are ".format(n, ))
while n>1:
    if n%d ==0 :
        print(d)
        n=n/d
        continue
    d+=1

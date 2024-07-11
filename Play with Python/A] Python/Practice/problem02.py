n = 5
sum = 0
while(n > 0):
  sum = sum + n
  n -= 1

print(sum)

#using function 

def sum(n):
  sum=0
  while n>0:
      sum = sum+n
      n-=1
  return sum
  
print(sum(5))

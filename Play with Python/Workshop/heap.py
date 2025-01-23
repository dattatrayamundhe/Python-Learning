import heapq

a = [10, 20, 4, 45, 99]

# Get the two largest numbers using heapq.nlargest
top_two = heapq.nlargest(2, a)

# The second largest number is at index 1
print(top_two[1])
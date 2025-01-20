from itertools import groupby

# Example list with consecutive duplicates

s = [1, 1, 2, 3, 3, 4]

# Removing consecutive duplicates using groupby

res = [key for key, _ in groupby(s)]
print(res)
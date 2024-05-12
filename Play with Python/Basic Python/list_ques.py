lst = ["HS001","TW0012","RT1256"]
for a in lst:
    p1 = set(a)
    p2 = set(a)
    p3 = set(a)

    q = {1,2,3,4,5,6,7,8,9}

    r1 = p1.intersection(q)
    r2 = p2.intersection(q)
    r3 = p3.intersection(q)

    print(r1 ,"\n", r2 ,"\n", r3 )


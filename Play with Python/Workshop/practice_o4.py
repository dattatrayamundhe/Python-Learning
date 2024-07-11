def insertIntoList(L,x,y):
        L.insert(x,y)
        
N = int(input())
L = []
for i in range(N):
        query = input()
        if (query.find("insert")>=0):
                a = query[7:]
                x,y = a.split()
                x = int(x)
                y = int(y)
                insertIntoList(L,x,y)
        
        elif (query.find("remove")>=0):
                 b = query[7:]
                 b = int(b)
                 L.remove(b)


        elif (query.find("print")>=0):
                 print(L)
        
        elif (query.find("append")>=0):
                 c = query[7:]
                 c = int(c)
                 L.append(c)

        elif (query.find("sort")>=0):
                L.sort()

        elif (query.find("pop")>=0):
                L.pop(-1)

        elif (query.find("reverse")>=0):
                L.reverse()
        
        
                

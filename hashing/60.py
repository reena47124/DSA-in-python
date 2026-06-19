#hashing
#find first duplicate
a=[1,2,3,2,3,4,5]
seen=set()
for x in a:
    if x in seen:
        print(x)
        break
    else:
        seen.add(x)
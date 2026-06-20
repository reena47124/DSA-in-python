#hashing
#find all duplicates
a = [1,2,2,3,4,4]
seen = set()
duplicates = []
for x in a:
    if x in seen:
        duplicates.append(x)
    else:
        seen.add(x)
print(duplicates)
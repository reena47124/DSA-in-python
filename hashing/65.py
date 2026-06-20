#hashing
#find unique elements
a = [1,2,2,3,3,4]
freq = {}
for x in a:
    freq[x] = freq.get(x,0) + 1
for key, value in freq.items():
    if value == 1:
        print(key)
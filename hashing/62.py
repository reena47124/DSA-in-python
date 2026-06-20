#hashing
#first non-repeating element
a = [1,2,2,3,3]
freq = {}
for x in a:
    freq[x] = freq.get(x,0) + 1
for x in a:
    if freq[x] == 1:
        print(x)
        break
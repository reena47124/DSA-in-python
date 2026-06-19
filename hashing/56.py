#hashing
#count frequency of elements
a=[1,2,2,3,4,2,3,3,4]
freq={}
for num in a:
    freq[num]=freq.get(num,0)+1
print(freq)    
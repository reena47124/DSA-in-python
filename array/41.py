#array
#linear search
a=[1,3,5,7,9]
ele=7
for i in range(len(a)):
    if a[i]==ele:
        print(f"element found at:{i}")
        break
else:
    print(f"element doest exist,-1")
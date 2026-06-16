#array
#delete an element from an array,from the beginning,using built-in method
a=[2,4,6,8,10]
print("array before deletion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
print()
del a[0]
print("array after deletion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
        
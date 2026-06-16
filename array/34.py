#array
#delete an element from an array,from a giving position,using built-in method
a=[2,4,6,8,10]
pos=2
print("array before deletion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
print()
del a[pos-1]
print("array after deletion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")    
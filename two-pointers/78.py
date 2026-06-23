#two-pointer
#dutch national flag problem
def func_dutch(a):
    c0=0
    c1=0
    c2=0
    for num in a:
        if num==0:
            c0+=1
        elif num==1:
            c1+=1
        else:
            c2+=1
    pos=0
    for i in range(c0):
        a[pos]=0 
        pos+=1
    for i in range(c1):
        a[pos]=1
        pos+=1
    for i in range(c2):
        a[pos]=2
        pos+=1
    return a
a=[0,1,2,0,1,2,2,1,2]
print(func_dutch(a))                           
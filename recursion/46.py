#recursion
#fibonacci series
def fibo(n):
    if n==0:
        return 0
    elif (n==1 or n==2):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=6
print(f"fibonacci series upto {n}th term:",end="")
for i in range(n):
    print(fibo(i),end=" ") 
print()    
print(f"the {n}th term of the fibonacci series is:{fibo(n-1)}")    

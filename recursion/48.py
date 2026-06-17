#recursion
#print downward right angle triangle with stars.
def fun(n):
    for i in range(n):
        print("*",end=" ")
    print()
    if n>1:
        fun(n-1)
fun(5)            
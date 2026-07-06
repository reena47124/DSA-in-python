#bit manipulation
#compute XOR from 1 to n,optimize approach.
def compute_XOR(n):
    if n%4==0:
        return n
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    return 0
print(compute_XOR(5))


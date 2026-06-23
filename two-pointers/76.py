#two-pointer
#reverse a string without altering the position of the space.naive approach
def reverse_string(s):
    chars=[ch for ch in s if ch!=' ']
    chars.reverse()
    result=[]
    for ch in s:
        if ch==' ':
            result.append(' ')
        else:
            result.append(chars.pop(0))
    return ''.join(result)
s="hello there!"
print(reverse_string(s))            
    
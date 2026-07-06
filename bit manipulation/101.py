#bit manipulation
#set a bit at nth position.
def set_bit(num,pos):
    num=num|(1<<pos)
    return num
num=0
pos=0
print(set_bit(0,0))
num=8
pos=1
print(set_bit(8,1))
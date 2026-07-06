#bit manipilation
#right-shift
num1=20
print(f"decimal num1:{num1}")
bt1=bin(num1)[2:].zfill(8)
print(f"binary num1:{bt1}")
num2=num1>>1
print(f"decimal num2:{num2}")
bt2=bin(num2)[2:].zfill(8)
print(f"binary num2:{bt2}")
num3=num1>>2
print(f"decimal num3:{num3}")
bt3=bin(num3)[2:].zfill(8)
print(f"binary num3:{bt3}")
num4=num1>>3
print(f"decimal num4:{num4}")
bt4=bin(num4)[2:].zfill(8)
print(f"binary num4:{bt4}")
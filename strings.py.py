angle1 = int(input("enter the angle1: "))
angle2 = int(input("enter the angle2: "))
angle3 = int(input("enter the angle3: "))

if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0 :
    print("it is a triangle")
    
else:
    print("it is not a triangle")
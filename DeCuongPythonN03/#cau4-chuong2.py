#cau4-chuong2
import math
a, b, c = map(int, input().split())
delta = b * b - 4 * a * c 
if a == 0:
    if b == 0:
        if c == 0:
            print("VSN") 
        else:
            print("VN") 
    else:
        print(f"x = {-c / b:.2f}")
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x1 = -b / (2 * a)
        print(f"x1 = x2 = {x1:.2f}")
    else:
        print("VN")

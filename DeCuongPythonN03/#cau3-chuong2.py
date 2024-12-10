#cau3-chuong2
import math
a, b, c = map(int, input().split())
delta = b * b - 4 * a * c 
if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
elif delta == 0:
        x1 = -b / (2 * a)
        print(f"x1 = x2 = {x1:.2f}")
else:
        print("VN")

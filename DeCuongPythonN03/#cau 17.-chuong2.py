#cau 17
import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())

a = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
b = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
c = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
s = (a + b + c) / 2

if a+b>c and a+c>b and b+c>a:
       print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
   
    
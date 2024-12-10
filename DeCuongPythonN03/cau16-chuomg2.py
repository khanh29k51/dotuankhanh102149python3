import math
a,b,c = map(int,input().split())
s = (a+b+c)/2
if a+b>c and a+c>b and b+c>a:
       print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
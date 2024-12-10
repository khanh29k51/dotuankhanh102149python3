#cau10-chuong2
import math
n ,x=map(int,input().split())
t =0
for i in range (n):
     t+=math.sqrt(x+t)
print(t+1)
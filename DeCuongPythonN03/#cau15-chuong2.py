#cau15-chuong2
x = float(input())
ep = float(input())
s = 1
n = 1
t= 1 
while abs(t) >= ep:
    t *= x / n 
    s += t 
    n += 1 
print(s)

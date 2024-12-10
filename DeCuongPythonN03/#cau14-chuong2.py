#cau14-chuong2
a = float(input())
s = 1  
n = 1 
x = 1
while True:

    if n > 1:
        x *= (2 * n - 1) * (2 * n)  
    t = 1 / x
    if t < a:
        break
    s += t
    n += 1
print(s)

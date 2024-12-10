#cau7-chuong2
n = int(input())
s = 0
for i in range (1,n+1):
    a=1 / (i*(i+1))
    s+=a
print(s)
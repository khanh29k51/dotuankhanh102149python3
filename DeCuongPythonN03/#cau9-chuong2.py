#cau9-chuong2
n,x = map(int,input().split())

s = x + 1

for i in range (2,n+1):
    x*=i
    s+=x
print(s)
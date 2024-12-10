#cau11-chuong2
n =  int(input())
s =1
for i in range (2,n+1):
    for a in range (1,i):
        a=a*(a+1)
    s+=a
print(s)


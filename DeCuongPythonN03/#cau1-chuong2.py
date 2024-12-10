#cau1-chuong2
a, b = map(int,input().split())
if b == 0:
    if a == 0:
        print("phuong tring vo so nghiem")
    else:
        print("x=0")
else:
    if a == 0:
        print("phuong trinh vo nghiem")
    else:
        print("x=",-b/a)

#cau12-chuong2
n = int(input())

s = 0

for i in range(1, 2 * n + 2, 2):
    a = 1
    for j in range(1, i + 1):
        a *= j
    s += a

print(s)

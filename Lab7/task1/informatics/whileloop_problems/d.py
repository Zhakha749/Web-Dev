N = int(input())
num = N

while num % 2 == 0:
    num //= 2

if num == 1:
    print("YES")
else:
    print("NO")
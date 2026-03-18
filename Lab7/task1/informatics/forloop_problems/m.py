N = int(input())
count = 0

for _ in range(N):
    n = int(input())
    if n == 0:
        count += 1

print(count)
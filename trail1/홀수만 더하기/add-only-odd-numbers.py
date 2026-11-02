N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0
for i in A:
    if i%2 == 1 and i%3 == 0:
        ans += i
print(ans)


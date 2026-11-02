A, B = map(int, input().split())

ans = 0
if A < B:
    for i in range(A, B+1):
        if i%5 == 0:
            ans += i
else:
    for i in range(B, A+1):
        if i%5 == 0:
            ans += i
print(ans)
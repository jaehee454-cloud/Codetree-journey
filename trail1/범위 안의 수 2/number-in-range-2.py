N = [int(input()) for _ in range(10)]

ans = 0
cnt = 0
for i in N:
    if 0 <= i <= 200:
        ans += i
        cnt += 1

ans_avg = ans / cnt
print(ans, f"{ans_avg:.1f}")
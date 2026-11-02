A, B = map(int, input().split())

ans_sum = 0
ans_div = 0
cnt = 0
for i in range(A, B+1):
    if i%5 == 0 or i%7 == 0:
        ans_sum += i
        cnt += 1
ans_div = ans_sum/cnt

print(ans_sum, f"{ans_div:.1f}")


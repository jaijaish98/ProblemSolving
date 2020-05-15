n = int(input())
s = input()
ans = [0] * 2
for i in range(n):
    g = ((int(s[i]) + i) % 2)
    ans[int(g)] += 1

print(min(ans[0], ans[1]))

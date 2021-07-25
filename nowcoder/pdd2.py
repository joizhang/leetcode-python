line = input()
s1, s2 = line.split()
n1, n2 = len(s1), len(s2)
ans_v = [0] * (n1 + n2)
for i in reversed(range(n2)):
    right = int(s2[i])
    for j in reversed(range(n1)):
        left = int(s1[j])
        total = ans_v[i + j + 1] + right * left
        ans_v[i + j + 1] = total % 10
        # 注意是+=
        ans_v[i + j] += total // 10

ans = ''
for i in range(len(ans_v)):
    if i == 0 and ans_v[i] == 0:
        continue
    ans += str(ans_v[i])
print(ans)

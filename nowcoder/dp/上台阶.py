n = int(input())

m_arr = []
for i in range(n):
    m_arr.append(int(input()))


def jump(m_):
    if m_ <= 3:
        return m_ - 1
    memo = [1, 2]
    for idx in range(4, m_ + 1):
        memo[0], memo[1] = memo[1], memo[0] + memo[1]
    return memo[-1]


for m in m_arr:
    print(jump(m))

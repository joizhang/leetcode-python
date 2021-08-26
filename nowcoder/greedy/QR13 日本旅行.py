nums = list(map(int, input().split()))
price = nums[-1]
coins = nums[:-2]
value = [1, 5, 10, 50, 100, 500]
# print(coins)
# 钱从大到小一枚一枚加起来就行了，直到等于A为止
count, i, flag = 0, 5, False
while price > 0:
    if i < 0:
        break

    if nums[i] == 0 or value[i] > price:
        i -= 1
        continue

    price -= value[i]
    nums[i] -= 1
    count += 1
    if price == 0:
        flag = True
        break
if flag:
    print(count)
else:
    print('NOWAY')

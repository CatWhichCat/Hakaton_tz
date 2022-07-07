prices = [7, 1, 5, 3, 6, 4]
i = 0
while i < len(prices) - 1:
    j = i + 1
    # print(i, prices[i])
    while j < len(prices):
        d = prices[j] - prices[i]
        print(f'prices[{j}] - prices[{i}] = {d}')
        j += 1
    i += 1
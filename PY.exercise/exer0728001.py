# -*- coding: utf-8 -*-

prices = {
    'acme':45.34,
    'AAPL':615.78,
    'IBM':205.50,
    'HPQ':37.20,
    'FB':19.88,
}

prices2 = {
    'ACME':45.66,
    'AAPL':612.78,
    'IBMD':25.50,
    'HPQ':37.20,
    'HPDD':322.21,
    'FB':10.88,
    'XCDO':9.041,
}

# MaxPrice = sorted(prices.items(),key = lambda s:s[1])[-1]
# MinPrice = sorted(prices.items(),key = lambda s:s[1])[0]
#
# print('max price stock is : ', MaxPrice)
# print('min price stock is : ', MinPrice)
#
# NewPrices = {key:prices[key] for key in prices.keys() - {'FB'}}
# print(NewPrices)

# print({key[0]:key[1] for key in set(prices.items()).union(set(prices2.items()))})
# # print(set(prices))
# print(set(prices.items()).union(set(prices2.items())))

for key in prices2:
    if(key not in prices):
        prices[key] = prices2[key]

print(prices)
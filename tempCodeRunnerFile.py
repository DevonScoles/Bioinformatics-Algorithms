def RecursiveChange(money, change):
#     if money == 0:
#         return 0
#     MinNumCoins = float('inf')
    
#     for i in range(0,len(change)):
#         coin = change[i]
#         if money >= coin:
#             NumCoins = RecursiveChange(money - coin, change)
#             if NumCoins + 1 < MinNumCoins:
#                 MinNumCoins = NumCoins + 1
#     return MinNumCoins

# RecursiveChange(money,change)
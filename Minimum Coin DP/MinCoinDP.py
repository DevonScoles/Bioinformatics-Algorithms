""" 
    This python script deals with the basic dynamic programming problem
    called minimum coin change
    given a text file with
    40
    1,5,10,20,25,50

    40 representing the amoung we want
    the list below representing the list of coins available to sum to that amount

"""
with open('MinCoin_dataset.txt','r') as file:
    lines = file.readlines()
money = int(lines[0])
# change = lines[1].split(',')
Coins = [int(i) for i in lines[1].split(',')]


def DPChange(money, Coins):
    if money == 0:
        return 0

    res = float('inf')
    for i in range(0, len(Coins)):
        if (Coins[i] <= money):
            sub_res = DPChange(money-Coins[i],Coins)
 
            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != float('inf') and sub_res + 1 < res):
                res = sub_res + 1
 
    return res

print(DPChange(money,Coins))

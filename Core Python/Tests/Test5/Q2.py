# A teacher came to class with a large box tokhat has
# several coins. Each coin has a number printed on it.
# Before coming to class, she ensured that All the
# numbers occur an Even number of times. However,
# while coming to the class, one coin fell down and got lost. 
# She wants to find out the number on the missing coin.
# Inputs:
# The original number of coins and the actual
# number on each of the coins, separated by spaces.
# Output: The number on the missing coin
# Sample Input: 8
# 5 7 2 7 5 2 5
# Sample Output: 5

def find_missing_coin(str1):
    data = list(map(int, str1.split()))
    remaining_coins = data[1:]
    
    missing_coin = 0
    for coin in remaining_coins:
        missing_coin ^= coin
        
    return missing_coin

sample_input = "8 5 7 2 7 5 2 5"
print(find_missing_coin(sample_input))  # Output: 5

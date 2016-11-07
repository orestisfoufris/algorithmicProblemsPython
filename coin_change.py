'''
Problem statement:

You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

'''

def solve(coins, s):
   dp = [sys.maxint] * (s + 1)
   dp[0] = 0
   for coin in coins:
       for i in range(coin, s + 1):
           if dp[i - coin] != sys.maxint:
               dp[i] = min(dp[i], dp[i - coin] + 1)
   return -1 if dp[s] == sys.maxint else dp[s]

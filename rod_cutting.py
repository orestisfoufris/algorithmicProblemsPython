'''
classic rod-cutting dynamic programmming problem
as seen on CLRS
'''
import sys
import math

INT_MIN = -sys.maxint - 1

def rod_cutting_bottom_up(lengths, prices, n):
    dp = [0] * (n + 1)
    dp[1] = prices[0]

    for i in range(1, n):
        dp[i + 1] = prices[i]
        for k in range(i):
            dp[i + 1] = max(dp[i + 1], dp[i - k] + prices[k])

    return dp[n]

def rod_cutting_solve_top_down(lengths, prices, n, dp):
    if n <= 0:
        return 0

    if dp.get(n) != None:
        return dp.get(n)

    max_value = INT_MIN
    for i in range(n):
        max_value = max(max_value, prices[i]
        + rod_cutting_solve_top_down(lengths, prices, n - i - 1, dp))

    dp[n] = max_value
    return max_value


if __name__ == '__main__':
    lengths = [1,2,3,4,5,6,7,8,9,10]
    prices = [1,5,8,9,10,17,17,20,24,30]
    print rod_cutting_solve_top_down(lengths, prices, 7, {})
    print rod_cutting_bottom_up(lengths, prices, 7)


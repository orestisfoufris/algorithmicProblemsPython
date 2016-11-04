'''
Burst Balloons dynamic programming problem
https://leetcode.com/problems/burst-balloons/
'''

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # let's put the 1s before and after
    nums = [1] + nums + [1]

    N = len(nums)

    # dp[i][j] denotes the best result for range (i, j)
    dp = [[0 for i in range(N)] for i in range(N)]

    for i in range(1, N - 1):
        for left in range(0, N - i - 1):
            # starting point for right
            right = left + i + 1
            # m (middle) will be the last balloon
            # to be burst
            for m in range(left + 1, right):
                dp[left][right] = max(dp[left][right], dp[left][m] +
                dp[m][right] + nums[left] * nums[m] * nums[right])

    return dp[0][N - 1]

'''
longest increasing subsequence problem
'''

def lis(array):
    result = 1
    if len(array) == 0:
        return 0

    dp = [1] * (len(array) + 1)
    for i in xrange(1, len(array)):
        for j in xrange(i):
            if array[i] > array[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                result = max(result, dp[i])
    return result

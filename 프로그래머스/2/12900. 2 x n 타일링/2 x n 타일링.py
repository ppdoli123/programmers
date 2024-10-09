import math
# 1 2 3 5 8 13 21
def solution(n):
    answer = 0
    res = 1
    com = 2
    dp = [1,2]
    for e in range(2,n):
        dp.append((dp[e-2]+dp[e-1])% 1000000007)

    
    return dp[n-1]
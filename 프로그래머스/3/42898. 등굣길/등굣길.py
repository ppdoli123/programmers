def solution(m, n, puddles):
    answer = 0
    t = []
    a="asd"
    dp = [[0 for i in range(m)] for j in range(n)]
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1
        
    for i in range(m):
        if dp[0][i] != -1:
            dp[0][i] = 1
        else:
            break
    for i in range(n):
        if dp[i][0] != -1:
            dp[i][0] = 1
        else:
            break
            
    for x in range(1,n):
        for y in range(1,m):
            if dp[x][y] == 0 :
                if dp[x-1][y] == -1:
                    dp[x][y] = dp[x][y-1]
                elif dp[x][y-1] == -1:
                    dp[x][y] = dp[x-1][y]
                else:
                    dp[x][y] = dp[x-1][y] + dp[x][y-1]
                    
    return dp[-1][-1]%1000000007
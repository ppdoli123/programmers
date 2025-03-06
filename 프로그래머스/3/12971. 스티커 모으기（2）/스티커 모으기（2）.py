import collections
def solution(sticker):
    #원형 양옆은 못뜯고 길이는 100000 숫자 100이하 첫번쨰랑 마지막은 연결 따로 생각ㅎ
    #bfs 가 맞는듯 ? 아니면 3개씩
    t = []
    if len(sticker) == 1:
        return sticker[0]
    if len(sticker) == 2:
        return max(sticker[0], sticker[1])
    dp = [0]*len(sticker)
    idx = 2
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    while idx+1 < len(sticker):
        dp[idx] = max(dp[idx-1], dp[idx-2] + sticker[idx])
        idx += 1
    t.append(dp[-2])
    dp = [0]*len(sticker)
    idx = 2
    dp[0] = 0
    dp[1] = sticker[1]
    while idx < len(sticker):
        dp[idx] = max(dp[idx-1], dp[idx-2] + sticker[idx])
        idx += 1
    t.append(dp[-1])
    return max(t)
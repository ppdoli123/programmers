def solution(players, callings):
    answer = []
    thr = ""
    score= {}
    for i in range(len(players)):
        score[players[i]] = i

    for name in callings:
        n = score[name]
        score[players[n-1]] += 1
        score[name] -= 1
        
        # e = players[n-1]
        # players[n-1] = players[n]
        # players[n] = e
        players[n] , players[n-1] = players[n-1] , players[n]
        
    score = sorted(score.items(), key=lambda x: x[1])

    return [item[0] for item in score]
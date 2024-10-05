def solution(diffs, times, limit):
    # 숙련도를 exp
    # 시간을 time
    
    max_exp = max(diffs)
    low, high = 1, max_exp
    
    while low <= high:
        exp = (low + high) // 2
        time = times[0]
        
        for i in range(1, len(times)):
            # 난이도가 더 높을 때
            if exp < diffs[i]:
                time += (times[i-1] + times[i]) * (diffs[i] - exp) + times[i]
            # 난이도가 작거나 같을 때
            else:
                time += times[i]
        
        if time <= limit:
            result = exp  # 현재 exp가 가능한 답이므로 저장
            high = exp - 1  # 더 작은 exp 탐색
        else:
            result = exp +1
            low = exp + 1  # 더 큰 exp 탐색
    
    return result 

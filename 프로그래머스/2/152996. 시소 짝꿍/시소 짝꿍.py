from collections import deque , Counter
#지금 10 20, 10 20 이 두개가 떠야되는데 하나만 뜨는 오류 발생함

def solution(weights):
    answer = 0
    
    weights_counter = Counter(weights)
    weights_set = list(set(weights))
    weights_set.sort(reverse=True)
    for weight in weights_counter:
        answer += int((weights_counter[weight] * (weights_counter[weight]-1))/2)
        answer += (weights_counter[weight] * weights_counter[weight/2])
        answer += (weights_counter[weight] * weights_counter[weight/1.5])
        answer += (weights_counter[weight] * weights_counter[weight/4*3])
    # print(Counter(weights))
    # answer = 0
    # weights=sorted(weights)
    # weights = deque(weights)
    # while weights:
    #     num = weights.popleft()
    #     if num in weights:
    #         answer += 1
    #     if int(num*2) in weights:
    #         answer += 1
    #     if int(num*1.5) in weights:
    #         answer += 1
    #     if int(num*(4/3)) in weights:
    #         answer += 1
    return answer
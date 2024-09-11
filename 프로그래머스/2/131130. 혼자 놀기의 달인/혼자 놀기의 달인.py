#cards 가 어쨋든 제대로 찾아가면 그룹이 반복문이 종료될거임

def solution(cards):
    answer = 0
    result = []
    num_current = []
    for i in range(len(cards)):
        num_first = cards[i]
        if num_first in num_current:
            continue
        while cards[num_first-1] not in num_current:
            past = len(num_current)
            num_first = cards[num_first-1]
            num_current.append(num_first)
        result.append(len(num_current))
        
    if len(result) == 1:
        return 0
    else:
        for e in range(len(result)-1,0,-1):
            result[e] -= result[e-1]
        result.sort(reverse=True)
    return result[0]*result[1]
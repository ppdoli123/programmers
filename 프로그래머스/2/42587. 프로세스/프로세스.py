import queue

def solution(priorities, location):
    answer = []
    q = [i for i in range(len(priorities))]
    while True:
        ans = q.pop(0)
        other_max = 0
        ma = max(priorities)  
        if priorities[ans] < ma:
            q.append(ans)
        else: 
            answer.append(ans)
            priorities[ans] = -1
        if len(q) == 0 :
            break
    return answer.index(location)+1
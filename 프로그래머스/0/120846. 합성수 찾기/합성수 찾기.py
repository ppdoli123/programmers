import math
def solution(n):
    answer = 0
    for i in range(n+1):
        for e in range(2,int(math.sqrt(i))+1):
            if i%e == 0:
                answer +=1 
                break
    return answer
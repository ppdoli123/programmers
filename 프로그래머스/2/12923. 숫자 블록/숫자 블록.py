import math
def solution(begin, end):
    result = []
    answer = [0]

    for i in range(begin,end+1):
        n = 0
        for e in range(2,int(math.sqrt(i))+1):
            if i%e == 0 and e <= 1e7:
                n = e
                if i // e <= 1e7:
                    n = i // e
                    break
        if n == 0 :
            n = 1
        result.append(n)
        
    if begin == 1:
        result[0]=0
        
    return result
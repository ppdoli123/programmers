import itertools
import math
def solution(numbers):
    answer = 0
    arr = []
    for e in range(1,len(numbers)+1):
        for li in itertools.permutations(numbers,e):
            num = ''.join(li)
            if int(num) not in arr:
                arr.append(int(num))
                
    if 0 in arr:
        arr.remove(0)
    if 1 in arr:
        arr.remove(1)
    for cor in arr:
        aa = 1
        for q in range(2,int(math.sqrt(cor))+1) :
            if cor % q == 0:
                aa = 0
                break
        if aa == 1:
            answer +=1
    return answer
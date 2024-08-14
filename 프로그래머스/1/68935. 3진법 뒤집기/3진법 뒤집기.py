import math

def solution(n):
    answer = 0
    num = ""
    while True:
        if n < 3:
            num += str(int(n))
            break
        
        num += str(int(n%3))
        n = n/3
        
    for i in range(len(num)):
        answer += int(num[i])*math.pow(3,len(num)-i-1)
    return answer

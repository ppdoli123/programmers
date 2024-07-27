def solution(numbers):
    answer = []
    lastBig=[]
    for i in reversed(numbers):
        while len(lastBig)>0: #스택
            if lastBig[-1]>i:
                answer.append(lastBig[-1])
                lastBig.append(i)
                break
            else:
                lastBig.pop(-1)
        if len(lastBig)==0:
            lastBig.append(i)
            answer.append(-1)
    return answer[::-1]
def solution(s):
    answer = []

    a=tuple(s)
    to = ""
    
    for i in range(len(a)):
        if a[i].isdigit():
            if a[i+1].isdigit():
                to += a[i]
            else:
                to += a[i]
                answer.append(to)
                to = ""
    answer.sort()
    max = answer[0]
    setu = set(answer)
    answers = [0]*len(setu)
    for se in setu:
        num = len(set(answer))
        for e in answer:
            if se == e:
                num -= 1
        answers[num]=int(se)
    return answers
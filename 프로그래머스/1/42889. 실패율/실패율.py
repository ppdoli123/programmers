def solution(N, stages):
    answer = []
    dic = {}
    number = len(stages)
    i = 1
    while True:
        co = stages.count(i)
        if number != 0:
            dic[i] = co/number
        else:
            dic[i] = 0
        number -= co
        i += 1
        if i == N + 1 :
            break
    answer = list(map(lambda x: x[0], sorted(dic.items(), key=lambda x: x[1], reverse=True)))
    return answer

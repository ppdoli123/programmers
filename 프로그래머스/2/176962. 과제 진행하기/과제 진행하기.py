def solution(plans):
    answer = []
    stack = []
    plans.sort(key = lambda x:x[1] )
    a,b = plans[0][1].split(":")
    time = int(a)*60+int(b)
    dic_c = {plans[0][0]:time}
    dic_e = {}
    for i in range(1,len(plans)):
        h,m = plans[i][1].split(":")
        current_time = int(h)*60 + int(m)
        dic_c[plans[i][0]] = current_time
        dic_c[plans[i-1][0]] -= current_time
        sub = int(plans[i-1][2]) + dic_c[plans[i-1][0]]
        if sub <= 0 :
            answer.append(plans[i-1][0])
            while sub <= 0 and stack:
                cur = stack[-1]
                dic_e[cur] += sub
                sub = dic_e[cur]
                if dic_e[cur] <= 0:
                    answer.append(stack.pop())
        else:
            dic_e[plans[i-1][0]] = sub
            stack.append(plans[i-1][0])
    answer.append(plans[i][0])
    while stack:
        answer.append(stack.pop())
    return answer
def solution(n, m, section):
    answer = 1
    stack = []
    stack.append(section[0])
    for i in range(len(section)):
        if section[i] - stack[0] >= m:
            stack = [section[i]]
            answer += 1
        else :
            stack.append(section[i])
        
    return answer
def solution(s):
    answer = 0
    first = 0
    another = 0
    f_str = s[0]
    for i in range(len(s)):
        
        if f_str == s[i]:
            first += 1
        else:
            another += 1
        if i == len(s)-1:
            answer+= 1
            break
        if first == another :
            answer += 1
            f_str = s[i+1]
            first,another = 0,0
        
    return answer
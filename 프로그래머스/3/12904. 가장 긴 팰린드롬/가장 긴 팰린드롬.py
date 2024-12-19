def solution(s):
    answer = 0
    #하나씩 넘어가면서 앞, 뒤 가 같으면 하나씩 더 + 기존 길이는 저장 그렇게 돌아가면 , n**2 
    tmp = []
    max_cnt = 1
    for st in s:
        tmp.append("#")
        tmp.append(st)
    tmp.append("#")
    if len(tmp) == 2:
        if tmp[0] == tmp[1]:
            return 2
        else:
            return 1
    # if s[::-1] == s:
    #     return len(s)
    for i in range(1,len(tmp)-1,1):
        num = 1
        cnt = 1
        if tmp[i-num] == tmp[i+num]:
            while i-num >= 0 and i+num <= len(tmp)-1:
                if tmp[i-num] == tmp[i+num]:
                    cnt += 2
                    num += 1
                else:
                    break
        elif tmp[i] == tmp[i-num] or tmp[i] == tmp[i+num]:
            cnt += 1
        
        else:
            cnt = 1
        if cnt > max_cnt:
            max_cnt = cnt
    return (max_cnt-1)/2
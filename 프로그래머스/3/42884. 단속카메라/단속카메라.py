def solution(routes):
    # 0 ~ 60000 10000대
    # 0 10 9 11
    # 도착시간 기준 솔트 치고 포문 돌려서
    routes.sort(key=lambda x:x[1])
    answer = 0
    idx = 0
    print(routes)
    while idx < len(routes)-1:
        num = routes[idx][1]
        for i in range(idx+1,len(routes)):
            if routes[i][0] > num or num > routes[i][1]:
                answer += 1
                print(routes[i],num)
                break
        idx = i
    return answer+1
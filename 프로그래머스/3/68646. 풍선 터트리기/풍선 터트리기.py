def solution(a):
    #번호가 작은건 한번만
    # 나머진 번호가 큰걸 없앰 bfs 이용해서 ㅊ첫번째를 
    if len(a) <= 2 :
        return len(a)
    else:
        answer = 2
    
    left = a[0]
    # right = min(a[2:])
    right = [0 for i in a]
    min_num = a[-1]
    for min_ in range(len(a)-1,-1,-1):
        right[min_] = min_num
        if min(min_num,a[min_]) == a[min_]:
            min_num = a[min_]
            
    for i in range(1,len(a)-1,1):
        if a[i] < left or a[i] < right[i]:
            answer += 1
        if left > a[i]:
            left = a[i]

        
    return answer

def solution(n):
    answer = []
    arr = [[0 for _ in range(n)] for _ in range(n)]
    t = 0
    total = 0
    start = 0
    mode = 0 
    result = 0
    q=0
    while True:
        total += 1
        if mode == 3:
            result += 1
            if int((n-1)/3) < result :
                break
            else:
                mode = 0
                total -= 2
        elif mode == 0 :
            if  t >= n or arr[t][start] != 0:
                mode = 1
                t -= 1
                total -= 1
            else:
                arr[t][start] = total
                t += 1
            
        elif mode == 1:
            q += 1
            if q >= n or arr[t][q] != 0:
                mode = 2
                q -=1
                total -= 1
            else:
                arr[t][q] = total
                
            
        elif mode == 2:
            if t - 1 < start or q - 1 < start or arr[t-1][q-1] != 0:
                mode = 3
                start += 1
                t = start * 2
                q = start 
            else:
                arr[t-1][q-1] = total
                t -= 1
                q -= 1
    for row in arr:
        for value in row:
            if value != 0:
                answer.append(value)
    return answer
def solution(rows, columns, queries):
    answer = []
    # 2차원 배열 생성
    # y1 ~ x1  y2 ~ x2  
    # 돌려
    # 반복

    arr = []
    total_arr = []
    for i in range(rows):
        arr = []
        for j in range(columns):
            arr.append((i)  * columns + j+1)
        total_arr.append(arr)
    for x1,y1,x2,y2 in queries:
        cur = total_arr[x1-1][y2-1]
        min_ = 100001
        for plus_x in range(y2-1,y1-1,-1): # 10 -> 9 9 -> 8
            total_arr[x1-1][plus_x] = total_arr[x1-1][plus_x-1]
            min_ = min(min_,total_arr[x1-1][plus_x])
        for minus_y in range(x1-1,x2-1): 
            total_arr[minus_y][y1-1] = total_arr[minus_y+1][y1-1]
            min_ = min(min_,total_arr[minus_y][y1-1])
        for minus_x in range(y1-1,y2-1):
            total_arr[x2-1][minus_x] = total_arr[x2-1][minus_x+1]
            min_ = min(min_,total_arr[x2-1][minus_x])
        for plus_y in range(x2-1,x1-1,-1): # 16 -> 10
            if plus_y == x1:
                total_arr[plus_y][y2-1] = cur
            else:
                total_arr[plus_y][y2-1] = total_arr[plus_y-1][y2-1]
            min_ = min(min_,total_arr[plus_y][y2-1])

        answer.append(min_)



        
    return answer
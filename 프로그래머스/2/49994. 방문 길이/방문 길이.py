def solution(dirs):
    answer = 0
    x_arr = [0]
    y_arr = [0]
    arr = [[]]
    for i in dirs:
        if i == "U":
            if y_arr[0] == 5:
                continue
            arr.append([(x_arr[0],y_arr[0]),(x_arr[0],y_arr[0] + 1)])
            y_arr[0] += 1
        elif i == "D":
            if y_arr[0] == -5:
                continue
            arr.append([(x_arr[0],y_arr[0]),(x_arr[0],y_arr[0]-1)])
            y_arr[0] -= 1
        elif i == "R":
            if x_arr[0] == 5:
                continue
            
            arr.append([(x_arr[0],y_arr[0]),(x_arr[0]+1,y_arr[0])])
            x_arr[0] += 1
        elif i == "L":
            if x_arr[0] == -5:
                continue
            arr.append([(x_arr[0],y_arr[0]),(x_arr[0]-1,y_arr[0])])
            x_arr[0] -= 1
    n = 0
    arr.pop(0)
    tuple_arr = [tuple(idx) for idx in arr]
    while n < len(arr)-1:
    
        for i in range(n+1,len(arr)):
            if set(tuple_arr[n]) == set(tuple_arr[i]):
                answer -= 1
                break
        n += 1
    answer += len(tuple_arr)
    return answer
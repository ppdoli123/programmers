def solution(places):
    answer = []
    number = len(places)
    width = len(places[0])
    height = len(places)
    for num in places:
        queue = []
        for i in range(height):
            for j in range(width):
                if num[i][j] == "P":
                    queue.append([i,j])
        if len(queue) == 0:
            answer.append(1)
            continue
            
        vaild = True
        while queue:
            target_x,target_y = queue.pop()
            for que_x,que_y in queue:
                x = abs(target_x - que_x ) 
                y = abs(target_y - que_y ) 
                if x+y == 1:
                    vaild = False
                    break
                if x+y == 2:
                    if x > 0 and y > 0 :
                        if num[target_x][que_y] != "X" or num[que_x][target_y] != "X":
                            vaild = False
                            break
                    elif x > 0:
                        result_x = int((target_x + que_x)/2)
                        if num[result_x][que_y] != "X":
                            vaild = False
                            break
                    elif y > 0 :
                        result_y = int((target_y + que_y)/2)
                        if num[que_x][result_y] != "X":
                            vaild = False
                            break
                
            if not vaild:
                break

        if vaild:
            answer.append(1)
        else:
            answer.append(0)
    return answer
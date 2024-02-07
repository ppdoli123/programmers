def solution(wallpaper):
    answer = []
    x= []
    y= []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                x.append(i)
                y.append(j)
    
    x.sort()
    y.sort()
    answer.append(x[0])
    answer.append(y[0])
    answer.append(x[-1]+1)
    answer.append(y[-1]+1)
    
    return answer
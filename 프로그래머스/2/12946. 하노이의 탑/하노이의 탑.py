def solution(n):
    answer= [[]]
    middle = []
    first = [[]]
    last = []
    # n = 1 [1,3]
    # n = 2 [1,2]   [1,3]   [2,3] 3
    # n = 3 [1,3][1,2][3,2]   [1,3]    [2,1] [2,3] [1,3] 7
    # n = 4 [1,2][1,3][2,3][1,2][3,1][3,2][1,2]  [1,3] [] 15
    
    t = 3
    middle = [[1,3]]
    first = [[1,2]]
    last = [[2,3]]
    if n == 1:
        return [[1,3]]
    if n == 2:
        return [[1,2],[1,3],[2,3]]
        
    while True:
        fir = first + middle + last
        las = first + middle + last
        for i in range(len(fir)):
            if fir[i] == [1,2]:
                fir[i] = [1,3]
            elif fir[i] == [1,3]:
                fir[i] = [1,2]
            elif fir[i] == [2,3]:
                fir[i] = [3,2]
            elif fir[i] == [3,2]:
                fir[i] = [2,3]
            elif fir[i] == [3,1]:
                fir[i] = [2,1]
            elif fir[i] == [2,1]:
                fir[i] = [3,1]
        for i in range(len(las)):
            if las[i] == [1,2]:
                las[i] = [2,1]
            elif las[i] == [1,3]:
                las[i] = [2,3]
            elif las[i] == [2,3]:
                las[i] = [1,3]
            elif las[i] == [3,2]:
                las[i] = [3,1]
            elif las[i] == [3,1]:
                las[i] = [3,2]
            elif las[i] == [2,1]:
                las[i] = [1,2]
        first = fir
        last = las
        if n == t:
            answer = fir + middle+ las
            break
        t+=1
    return answer
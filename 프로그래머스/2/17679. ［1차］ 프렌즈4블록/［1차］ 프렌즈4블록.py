def solution(m, n, board):
    answer = 0
    cor = []
    dimension = [[1,0],[1,1],[0,1]]
    
    while True:
        
        char =[]
        board = [list(row) for row in board]
        for x in range(0,m-1):
            for y in range(0,n-1):   
                cur = board[x][y]
                cur_check = True
                for dx,dy in dimension:
                    if board[x+dx][y+dy] != cur or board[x][y] == "0":
                        cur_check = False
                if cur_check == True:
                    char.append([x,y])
                    char.append([x+1,y])
                    char.append([x+1,y+1])
                    char.append([x,y+1])
        if len(char) == 0 :
            break
        for x,y in char:   
            board[x][y] = "0"

        i = 0
        while i < n :
            for x in range(m) :
                if board[x][i] == "0":
                    x_index = 1
                    while x > 0 :
                        board[x][i] = board[x-1][i]
                        board[x-1][i] = "0"
                        x -= 1
            i += 1
    for i in board:
        answer += i.count("0")
    return answer
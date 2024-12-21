def solution(board, skill):
    answer = 0
    #타입1이 - 2가 + , 첫번째가로, 첫번째세로, 두번째가로, 두번째세로, 대미지
    tmp = [[0 for i in range(len(board[0])+1)] for i in range(len(board)+1)]
    for type_,x1,y1,x2,y2,damage in skill:
        if type_ == 1:
            damage *= -1
            
        tmp[x1][y1] += damage
        if x2 + 1 < len(board):
            tmp[x2+1][y1] -= damage
        if y2 + 1 < len(board[0]):
            tmp[x1][y2+1] -= damage
        if x2 +1 < len(board) and y2 +1 < len(board[0]):
            tmp[x2+1][y2+1] += damage
            
    for nx in range(0,len(tmp),1):
        for ny in range(1,len(tmp[0]),1):
            tmp[nx][ny] += tmp[nx][ny-1]
    
    for dy in range(0,len(tmp[0]),1):
        for dx in range(1,len(tmp),1):
            tmp[dx][dy] += tmp[dx-1][dy]
            
    for dx1 in range(len(board)):
        for dy1 in range(len(board[1])):
            board[dx1][dy1] += tmp[dx1][dy1]
            if board[dx1][dy1] > 0:
                answer +=1
    return answer
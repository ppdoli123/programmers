# 01 10 32 23 4 개 가 가로 세로 대각선 기울기 1 0
def solution(n):
    answer = 0
    def safe(semi,col,row):
        for i in range(row):
            if semi[i] == col or \
               semi[i] - i == col - row or \
               semi[i] + i == col + row:
                return False
        return True
    def recursion(semi,num):
        nonlocal answer
        if num == n:
            answer += 1
            return 
        
        for idx in range(n):
            if safe(semi,idx,num):
                semi[num] = idx
                recursion(semi,num+1)
                
                
    semi = [-1]*n
    recursion(semi,0)
            
    return answer
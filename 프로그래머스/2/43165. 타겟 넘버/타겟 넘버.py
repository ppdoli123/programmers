
def dfs(number,i,total,target):
    global answer
    N = len(number)
    if i == N and total == target :
        answer += 1
        return

    if i == N:
        return
     
    dfs(number,i+1,total + number[i],target)
    dfs(number,i+1,total - number[i],target)
    
def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers,0,0,target)
    return answer
def solution(n, s):
    #아이디어 100000000c10000 무조건 시간복잡도 걸림
    #그럼 해결법은 이분탐색이긴 한데 처음엔 나머지가 0이면 같은걸로 다 하고 3 9 333 342
    answer = []
    
    #예외사항이 걸릴만한건 n > s 일때랑 
    if n > s :
        return [-1]
    
    
    if s%n == 0 :
        num = s//n
        answer = [num] * n
    else: 
        minus = s%n
        num = (s-minus)//n
        answer = [num] * (n-minus)
        for i in range(minus):
            answer.append(num+1)
        
    return answer
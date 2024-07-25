def solution(n, t, m, p):
    answer = ''
    correct = ""
    #n진법으로 변환하는게 필요
    for num in range(t*m):
        result = ""
        while True:
            if num >= n :
                result += str(change(num,n))
                num = int(num / n)
            else :
                result += str(change(num,n))
                break

        for num1 in range(len(result)-1,-1,-1):
            answer += result[num1]
    #t*m 시점까지
    #순서는 맨 마지막 /2
    
    for cor in range(p-1,t*m,m):
        correct += answer[cor]
    return correct

            
def change(num,n):
    if num % n < 10:
        ans = num % n
    elif num % n == 10:
        ans = 'A'
    elif num % n == 11:
        ans = 'B'
    elif num % n == 12:
        ans = 'C'
    elif num % n == 13:
        ans = 'D'
    elif num % n == 14:
        ans = 'E'
    elif num % n == 15:
        ans = 'F'
    return ans

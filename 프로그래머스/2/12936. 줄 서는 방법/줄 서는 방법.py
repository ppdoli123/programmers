
import math
def solution(n, k):
    fir = 0
    result = []
    num = [ i for i in range(1,n+1) ] 
    k -= 1 
    while n > 1 : 
        factorial = math.factorial(n-1)
        index = k//factorial
        k%= factorial
        
        result.append(num[index])
        n -= 1
        num.remove(num[index])
    
    result.append(num[0])
    return result
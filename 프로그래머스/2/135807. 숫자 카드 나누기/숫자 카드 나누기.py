import math
def solution(arrayA, arrayB):
    answer = ""
    arrA = [0]
    arrB = [0]
    boolA = True
    boolB = True
    for i in arrayA:
        arrA.append(math.gcd(i,arrA[-1]))
    maxA = arrA[-1]
    
    for i in arrayB:
        arrB.append(math.gcd(i,arrB[-1]))
    maxB = arrB[-1]
    
    if maxA != 1 :
        for i in arrayB:
            if i % maxA == 0 :
                boolA = False
    else:
        boolA = False
            
    if maxB != 1 :
        for i in arrayA:
            if i % maxB == 0 :
                boolB = False
    else:
        boolB = False
    
    if boolA == True and boolB == True:
        answer = max(maxA,maxB)
    elif boolB == True:
        answer = maxB
    elif boolA == True:
        answer = maxA
    else:
        answer = 0
        
    return answer
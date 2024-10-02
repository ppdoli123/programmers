# result < 0 이면 리턴
def solution(storey):
    answer = 0
    first= storey
    result = []
    length = len(str(storey))
    i = 1
    while i <= length:
        num = storey % (pow(10,i))
        if num < 5 * pow(10,i-1):
            answer += num / pow(10,i-1)
            storey -= num 
        elif num >= 5 * pow(10,i-1):
            answer += 10 - int(num / pow(10,i-1))
            storey += int(pow(10,i) - num)
        i += 1
    if result != 0 :
        result.append(answer+1)
    else:
        result.append(answer)
    answer = 0
    i = 1
    storey = first
    while i <= length:
        num = storey % (pow(10,i))
        if num <= 5 * pow(10,i-1):
            answer += num / pow(10,i-1)
            storey -= num 
        elif num > 5 * pow(10,i-1):
            answer += 10 - int(num / pow(10,i-1))
            storey += int(pow(10,i) - num)
        i += 1
    if storey != 0 :
        result.append(answer+1)
    else:
        result.append(answer)
    return min(result)
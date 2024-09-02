def solution(k, ranges):
    answer = [k]
    num = k
    result = []
    while num != 1:
        if num%2 == 0:
            num/=2
        else:
            num = num*3 + 1
        answer.append(num)
    for i,j in ranges:
        sum_num = 0
        if i > len(answer) + j - 1:
            result.append(-1)
        elif i == len(answer) + j - 1:
            result.append(0)
        else:
            while True:
                if i == len(answer)+j-1:
                    break
                sum_num += (answer[i]+answer[i+1])/2
                i+=1
            result.append(sum_num)
    return result
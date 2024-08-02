def solution(numbers):
    answer = []
    #0이 없는경우
    #마지막이 0 일경우
    for number in numbers:
        zero = -1
        bit_num = bin(number)[2:]
        for i in range(len(bit_num)):
            if bit_num[i] == '0':
                zero = i
        if len(bit_num)-1 == zero :
            answer.append(number+1)
        elif zero < 0:
            bit_num = bit_num[1:]
            bit_num = "10" + bit_num
            answer.append(int("0b"+bit_num,2))
        else:
            bit_num = bit_num[:zero]+"10"+ bit_num[zero+2:]
            answer.append(int("0b"+bit_num,2))
            
    return answer
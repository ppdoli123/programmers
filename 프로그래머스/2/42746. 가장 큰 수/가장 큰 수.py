import itertools
# 스택 만들고 넘버 배열에 첫자리로 정렬해
# 첫자리가 제일 큰거로 정렬 6 61 둘 셋 넷 까지 하는데 없으면 ? 가장 큰수 ? 9876 /1000
def solution(numbers):
    answer = ''
    count = 0
    num_arr = []
    for i in range(len(sorted(numbers))):
        trans_number = str(numbers[i])
        
        if numbers[i]//10 == 0: 
            trans_number += str(numbers[i])
        if numbers[i]//100 == 0:
            trans_number += str(numbers[i])
        if numbers[i]//1000 == 0:
            trans_number += str(numbers[i])
        num_arr.append([int(trans_number[:4]),i])
    num_arr.sort(key=lambda x:x[0],reverse=True)
    
    first_0 = True
    for number in num_arr:
        if first_0 == True and numbers[number[1]] == 0:
            break
        answer += str(numbers[number[1]])
        first_0 = False
    if len(answer) == 0:
        return "0"
    # stack = [str(i) for i in numbers]
    # if len(stack) == stack.count('0'):
    #     return "0"
    # while stack: 
    #     max_num = -1
    #     max_ = ""
    #     for i in stack:
    #         if max_num < int(int(i) / pow(10,len(i)-1)):
    #             max_num = int(int(i) / pow(10,len(i)-1))
    #             max_ = i
    #             print(max_,max_num,"1번")
    #         elif max_num == int(int(i) / pow(10,len(i)-1)):
    #             if len(max_) == len(i):
    #                 max_ = str(max(int(max_),int(i)))
    #                 print(max_,"3번")
    #         else:
    #             print(max_,i,"5번")        
    #     print(max_,"Asdf")
    #     stack.remove(max_)
    #     answer += max_
    return answer
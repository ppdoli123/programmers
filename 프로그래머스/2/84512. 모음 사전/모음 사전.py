def solution(word):
    answer = 0
    words = {'A': 0,'E':1,'I':2 ,'O':3,'U':4}
    for i in range(len(word)):
        sum_num = 0
        count = 0
        while count <= (4-i):
            sum_num += (5 ** count) 
            count += 1
            
        answer += (sum_num * words[word[i]]) + 1
        
    
    return answer
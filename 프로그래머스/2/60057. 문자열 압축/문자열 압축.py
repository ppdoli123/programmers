def solution(s):
    answer = 0
    dp = [-1] * int(len(s)/2)
    num = 1
    
    if len(s) == 1:
        return 1
    while num < int(len(s)/2)+1:
        extra = False
        string = ""
        first = ""
        grow_num = 1
        for i in range(0,len(s),num):
            if first == s[i:i+num]:
                extra = True
                grow_num += 1
            else:
                if extra == True:
                    extra = False
                    string = string + str(grow_num) + first
                    grow_num = 1
                else:
                    string += first
                first = s[i:i+num]
            if i == len(s) - num and extra == True:
                string = string + str(grow_num) + first 
                grow_num = 1
            elif i >= len(s) - num :
                string += first
        dp[num-1] = len(string)
        num += 1
    return min(dp)
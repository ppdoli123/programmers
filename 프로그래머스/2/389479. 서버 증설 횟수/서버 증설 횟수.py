def solution(players, m, k):
    answer = 0
    # m은 최소 사람
    # n*m <= m < (n+1)*m 
    # k시간동안 서버가 증설
    i = 0
    div = 0
    count_arr = [1] * 24
    
    while i < len(players):
        if players[i] < m*count_arr[i] :
            # print(i,"증설안됨")
            i += 1
        else:
            # print(i,players[i],m,count_arr[i],"증설됨")
            add_com = players[i] // m
            if count_arr[i] != 1:
                add_com -= count_arr[i]-1
            # print("증설" , i, add_com)
            for num in range(i,i+k):
                if num < len(players):
                    count_arr[num] += add_com 
                else:
                    break
            answer += add_com
            i+=1
    # print(count_arr)
            
        
    return answer
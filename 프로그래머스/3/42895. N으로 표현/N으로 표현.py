def solution(N, number):
    answer = 0
    #고려해야될게 n , nn , nnn , nnnn, nnnnn 8개 이상이면 -1
    # // +  - *  
    # 1 일때  n 
    # 2 일때 nn , n + n
    # 3 일때 1 + 2
    arr = [[0],[N]]
    idx = 2
    j = 0
    if N == number:
        return 1
    while len(arr) < 10 :
        nums = []
        for i in range(1,(idx//2)+1):
            j = idx - i
            if i != 0 and j != 0:
                for i_idx in range(len(arr[i])):
                    for j_idx in range(len(arr[j])):
                        if arr[i][i_idx] > arr[j][j_idx]:
                            nums.append(arr[i][i_idx] // arr[j][j_idx])
                            nums.append(arr[i][i_idx] - arr[j][j_idx])
                        elif arr[i][i_idx] < arr[j][j_idx]:
                            nums.append(arr[j][j_idx] // arr[i][i_idx])
                            nums.append(arr[j][j_idx] - arr[i][i_idx])
                        else:
                             nums.append(1)
                        nums.append(arr[i][i_idx] + arr[j][j_idx])
                        nums.append(arr[i][i_idx] * arr[j][j_idx])
                nums.append(int(str(N)*(idx)))
        arr.append(list(set(nums)))
        if number in arr[idx]:
            return idx
        idx+=1
        if idx == 10 :
            return -1
    
#     Num = [] 
#     for n in range(1,len(str(number))+1):
#         Num.append(N * int("1" *n))

#         Num.append(1*int("1" * n))
        
#     Num.sort()
#     length = len(Num)
#     Max = 0
#     Min = 0
#     MinMax = 50
#     division = -1
#     while MinMax != 0:
#         for i in range(length):
#             if Num[i] > number:
#                 Max = Num[i-1]
#                 Min = Num[i]
#                 MinMax = min(number - Max, Min - number)
#                 if MinMax == (number - Max) :
#                     if (i-1)%2 == 0:
#                         if division == 1:
#                             answer += (i-1)//2 + 1
#                             print("1이 두번 나온경우",i-1,answer)
#                         else:
#                             answer += (i-1)//2 + 2
#                             print("1이 두번 안나온 경우",i-1,answer)
#                         division = 1
#                     else:
#                         answer += (i-1)//2 + 1
#                         print("5가 나온경우")
#                 else:
#                     if i%2 == 0:
#                         if division == 1:
#                             answer += (i)//2 + 1
#                         else:
#                             answer += (i)//2 + 2
#                         division = 1
                        
#                     else:
#                         answer += i//2 + 1
#                 number = MinMax 
#                 break
            
#     if answer > 8 :
#         answer = -1
    return answer
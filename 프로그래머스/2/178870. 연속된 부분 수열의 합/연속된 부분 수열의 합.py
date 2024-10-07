def solution(sequence, k):
    answer = []
    cur = []
    dp = [[0,len(sequence)] for _ in range(len(sequence))]
    total = 0
    for i in range(len(sequence)-1,-1,-1):
        total += sequence[i]
        if total > k:
            total -= sequence.pop()
        elif total == k :
            while sequence[-1] == sequence[i-1] and i >0 :
                i -= 1
                sequence.pop()
            break
            # cur.append([i,len(sequence)-1])
    answer =  [i,len(sequence)-1]
    # print(cur)
    return answer
#         e = 0
#         if sequence[i]*(cur[1]+1) < k:
#             break
#         while i+e <= len(sequence)-1:
#             total += sequence[i+e]
#             if e > cur[1] :
#                 break
#             if total > k:
#                 dp[i] = [0,len(sequence)]
#                 break
#             elif total == k :
#                 dp[i] = [i,i+e]
#                 cur = [i,e]
#                 break
#             e+=1
#     answer = dp[cur[0]]
# #     if k in sequence:
# #         a=sequence.index(k)
# #         return [a,a]
# #     while i <= len(sequence):
# #         cor = [i]
# #         count += sequence[e]
# #         e += 1
# #         if count == k and e-i <= second - first:
# #             cor.append(e-1)
# #             answer.append(cor)
# #             count = 0
# #             i += 1
# #             e=i
# #             second = e
# #             first= i
            
#         if e == len(sequence) or count > k :
#             count = 0
#             i += 1
#             e = i
#         if i == len(sequence)-1:
#             break
    return answer
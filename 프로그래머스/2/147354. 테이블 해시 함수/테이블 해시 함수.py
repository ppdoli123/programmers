import collections
from functools import *
def solution(data, col, row_begin, row_end):
    answer = 0
    stack = [0]
    mod_sum = []
    
    for idx,two in enumerate(data[1:],start = 1):
        result = []
        n = []
        # [[1, 2, 3, 4], [1, 0, 1, 0], [0, 1, 0, 1], [7, 7, 7, 7]] ,2,2,3
        while len(stack) > 0 and data[stack[-1]][col-1] > two[col-1]:
            result.append(stack.pop())
        if len(stack) == 0 or data[stack[-1]][col-1] < two[col-1] :
            stack.append(idx)
        else :
            while len(stack) > 0 and data[stack[-1]][0] < two[0] and data[stack[-1]][col-1] == two[col-1] :
                n.append(stack.pop())
            stack.append(idx)
            for e in range(len(n)-1,-1,-1):
                stack.append(n[e])
            
        for i in range(len(result)-1,-1,-1):
            stack.append(result[i])
#     for mod in range(row_begin-1, row_end):
#         s = 0  # s를 각 mod에 대해 초기화
#         for i in range(len(data[0])):
#             s += data[stack[mod]][i] % (mod+1)
#         mod_sum.append(s)

#     answer = mod_sum[0]
#     for i in range(1, len(mod_sum)):
#         answer ^= mod_sum[i]  # XOR 연산
#     return answer
    return reduce(lambda x, y: x^y, [sum([d%(i+1) for d in data[stack[i]]]) for i in range(row_begin-1, row_end)])

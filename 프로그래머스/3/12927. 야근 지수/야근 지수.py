from collections import deque
import heapq
def solution(n, works):
    answer = 0
    minus = [-i for i in works]
    heapq.heapify(minus)
    while n > 0 :
        max_ = heapq.heappop(minus)
        if max_ == 0:
            heapq.heappush(minus,0)
        else:
            heapq.heappush(minus,max_+1)
        
        n -= 1
    for i in minus:
        answer += (i)**2
    # while n > 0:
    #     cnt = 0
    #     maxv = ans.popleft()
    #     if maxv == 0:
    #         return 0
    #     if maxv > ans[0]:
    #         n -= 1
    #         ans.append(maxv-1)
    #     elif maxv == ans[0]:
    #         n-=1
    #         ans.append(maxv-1)
    #     else:
    #         ans.append(maxv)
    #     print(ans)
    # print(ans)
    # for i in ans:
    #     answer += i**2
    return answer
from collections import deque
import heapq

def solution(n, k, enemy):
    answer = 0
    que = deque(enemy)
    heap = []
    dp = 0
    sum_ = 0
    count = 0
    if len(enemy) == k:
        return k
    for i in range(len(enemy)):
        sum_ += enemy[i]
        heapq.heappush(heap,(-enemy[i],enemy[i]))
        if sum_ > n:
            if count < k :
                count += 1
                sum_ -= heapq.heappop(heap)[1]
            else:
                return dp
        dp += 1
        
    return dp

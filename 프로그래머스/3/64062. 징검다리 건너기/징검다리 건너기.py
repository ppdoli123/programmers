
import collections
def solution(stones, k):
    #디딤돌 숫자 하나씩 줄어듬
    #0되면 못밟음
    #여러개면 무조건 가까운 디딤돌
    answer = 200000001
    tmp = collections.deque()
    # print(answer,tmp)
    for idx in range(len(stones)):
        tmp.appendleft((stones[idx],idx))
        while stones[idx] > tmp[-1][0]:
            tmp.pop()
        tmp.popleft()
        tmp.append((stones[idx],idx))
        if tmp[0][1] <= idx-k :
            tmp.popleft()
        if idx >= k-1:
            answer = min(answer,tmp[0][0])
        # print(answer, tmp)
        
    return answer
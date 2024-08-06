from collections import deque
def solution(queue1, queue2):
    answer = -1
    total = sum(queue1) + sum(queue2)
    limit = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    while True:
        if total%2 == 1:
            return -1
        answer += 1
        if answer > limit*3 :
            return -1
        if sum1 > int(total/2):
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
        elif sum1 < int(total/2):
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
        else:
            break
    return answer
from collections import deque
def solution(order):
    answer = 0
    #스택이용하고
    #오더랑 스택에서 하나씩 비교해서 뺴내면 될듯 ?
    stack = []
    order = deque(order)
    first = deque(i+1 for i in range(len(order)))
    while order:
        if len(first) == 0 :
            while stack and order[0] == stack[-1]:
                stack.pop()
                order.popleft()
                answer += 1
            break
        else:
            if order[0] != first[0]:
                if stack and order[0] == stack[-1]:
                    stack.pop()
                    order.popleft()
                    answer += 1
                else:
                    num = first.popleft() 
                    stack.append(num)
            else:
                first.popleft()
                order.popleft()
                answer += 1
    return answer
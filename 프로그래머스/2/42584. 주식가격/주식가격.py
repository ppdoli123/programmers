def solution(prices):
    answer = [-1 for i in range(len(prices))]
    stack = []
    t = 0
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            time = stack.pop()
            answer[time] = i - time 
        stack.append(i)
    while stack:
        last = stack.pop()
        answer[last] = i - last
    return answer
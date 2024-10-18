import heapq
def solution(operations):
    answer = []
    for i in operations:
        sol,num = i.split(" ")
        if sol == "I":
            heapq.heappush(answer,int(num))
        elif answer and sol == "D" and num == "-1":
            heapq.heappop(answer)
        elif answer and sol == "D" and num =="1":
            answer.remove(max(answer))

    if not answer:
        return [0,0]
    else:
        return [max(answer),min(answer)]
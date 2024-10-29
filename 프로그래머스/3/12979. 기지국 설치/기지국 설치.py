def solution(n, stations, w):
    answer = 0
    # visited 로 하는게 제일 좋아보이는데 ?
    # 
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    empty_slot = []
    zero = 0
    for i in stations:
        empty_slot.append([zero,i-w-2])
        zero = i+w
    if i+w < n :
        empty_slot.append([i+w,n-1])
    for first,last in empty_slot:
        num = last-first+1 
        answer += (num // (w*2+1))
        if num % (w*2+1):
            answer += 1
            
#     visited = [False] * n
#     for i in stations:
#         num = 0
#         if i-w < 0:
#             num = -(i-w)
#         if i+w > len(visited):
#             num =  (i+w) -len(visited) 
#         pre = [True] * (2*w+1 - num)
#         visited = visited[:i-w-1] +pre+ visited[i+w:]
        
#     idx = 0
#     while idx < n:
#         if False not in visited :
#             break
#         if visited[idx] == False:
#             pre = [True] * (2*w+1)
#             visited[idx:idx+(2*w+1)] = pre
#             idx += (2*w+1)
#             answer += 1
#         else:
#             idx += 1

    return answer
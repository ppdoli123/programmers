#2:28 ~
#우선 n진법으로 나열
#제일 처음 제일 마지막 따로 처리
# 중간에 0 으로 슬라이싱을 해야됨
import math
def solution(n, k):
    answer = 0
    mid = ""
    while True :
        mid += str(n%k)
        n = int(n / k)
        if n < k :
            mid += str(n%k)
            break
    mid = mid[len(mid)+1::-1]
    mid_arr = mid.split("0")
    for i in mid_arr:
        if len(i) == 0 or i =='1':
            answer += 1
            continue
        if i == "2" or i =="3":
            continue
        for num in range(2,int(math.sqrt(int(i)))+1):
            if int(i) % num == 0:
                answer += 1
                break
    print(answer)
    print(mid_arr)
    return  len(mid_arr) - answer
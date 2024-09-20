#3:20~
# 첫 자리 숫자는 이미 있고 , 두 자리부터 사전에 등록 , 다시  처음부터 반복

def solution(msg):
    answer = []
    string = [chr(i) for i in range(65,91)]
    i = 0
    while i < len(msg):
        num = 1
        while i+num <= len(msg):
            if msg[i:i+num] in string:
                num += 1
            else:
                string.append(msg[i:i+num])
                break
        answer.append(string.index(msg[i:i+num-1])+1)
        i += (num-1)
    return answer
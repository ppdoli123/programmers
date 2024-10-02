def solution(arr):
    answer = [0,0]
    tt = []
    #스택에 슬라이스한걸 넣고 하나씩 빼면서 다시 추가 
    length = len(arr)
    stack = []
    stack.append(arr)
    def check_all_same(matrix):
        first_value = matrix[0][0]
        return all(all(cell == first_value for cell in row) for row in matrix)

    # 초기 검사: 모든 값이 0이거나 1인 경우 바로 반환
    if check_all_same(arr):
        return [0, 1] if arr[0][0] == 1 else [1, 0]

    # if set(first) == 1:
    #     answer[arr[0][0]] += 1
    #     return answer
    while stack :
        target = stack.pop()
        length = len(target)
        if length == 1:
            answer[target[0][0]] += 1
        else:
            n = []
            uni = 0
            se = target[0][0]
            for i in range(int(length/2)):
                n.append(target[i][0:int(length/2)])
                if set(target[i][0:int(length/2)]) != {se}:
                    uni = 1
            if uni == 0:
                answer[target[i][0]] += 1
            else:
                stack.append(n)
            n = []
            uni = 0
            se = target[0][-1]
            for i in range(int(length/2)):
                n.append(target[i][int(length/2):])
                if set(target[i][int(length/2):]) != {se}:
                    uni = 1
            if uni == 0:
                answer[target[i][-1]] += 1
            else:
                stack.append(n)
            n = []
            uni = 0
            se = target[-1][0]
            for i in range(int(length/2),length):
                n.append(target[i][0:int(length/2)])
                if set(target[i][0:int(length/2)]) != {se}:
                    uni = 1
            if uni == 0:
                answer[target[i][0]] += 1
            else:
                stack.append(n)
            n = []
            uni = 0
            se = target[-1][-1]
            for i in range(int(length/2),length):
                n.append(target[i][int(length/2):])
                if set(target[i][int(length/2):]) != {se}:
                    uni = 1
            if uni == 0:
                answer[target[i][-1]] += 1
            else:
                stack.append(n)

    return answer
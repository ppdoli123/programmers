def solution(ingredient):
    answer = 0
    stack = []
    
    for ing in ingredient:
        stack.append(ing)
        
        # 스택의 마지막 4개의 요소가 [1,2,3,1]인지 확인
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            # 패턴이 발견되면 스택에서 제거
            stack[-4:] = []  # 슬라이싱을 통해 한 번에 제거
            answer += 1
    
    return answer

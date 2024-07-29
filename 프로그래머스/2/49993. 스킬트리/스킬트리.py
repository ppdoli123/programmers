def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_index = 0  # 현재 필요한 스킬의 인덱스를 가리킵니다.
        valid = True
        
        for char in skill_tree:
            if char in skill:
                if char == skill[skill_index]:
                    skill_index += 1
                else:
                    valid = False
                    break
        
        if valid:
            answer += 1
    
    return answer

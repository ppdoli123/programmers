import itertools

def solution(relation):
    rows = len(relation)
    columns = len(relation[0])

    # 모든 가능한 속성 조합 생성
    all_combinations = []
    for i in range(1, columns + 1):
        all_combinations.extend(itertools.combinations(range(columns), i))

    # 유일성 체크
    unique_combinations = []
    for combo in all_combinations:
        temp = [tuple(relation[row][col] for col in combo) for row in range(rows)]
        if len(set(temp)) == rows:
            unique_combinations.append(combo)

    # 최소성 체크
    candidate_keys = []
    for combo in unique_combinations:
        is_minimal = True
        for key in candidate_keys:
            if set(key).issubset(set(combo)):
                is_minimal = False
                break
        if is_minimal:
            candidate_keys.append(combo)

    return len(candidate_keys)
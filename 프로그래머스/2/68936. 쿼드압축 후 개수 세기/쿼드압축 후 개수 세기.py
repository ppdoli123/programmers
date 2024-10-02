def solution(arr):
    def compress(x, y, n):
        # 기저 조건: 1x1 크기의 영역
        if n == 1:
            return arr[x][y]
        
        # 4개의 부분으로 분할
        half = n // 2
        top_left = compress(x, y, half)
        top_right = compress(x, y + half, half)
        bottom_left = compress(x + half, y, half)
        bottom_right = compress(x + half, y + half, half)
        
        # 4개의 부분이 모두 같은 값이면 하나로 압축
        if top_left == top_right == bottom_left == bottom_right and isinstance(top_left, int):
            return top_left
        else:
            # 그렇지 않으면 4개의 결과를 리스트로 반환
            return [top_left, top_right, bottom_left, bottom_right]
    
    # 압축 결과
    result = compress(0, 0, len(arr))
    
    # 0과 1의 개수 세기
    def count_values(compressed):
        counts = [0, 0]
        if isinstance(compressed, int):
            counts[compressed] += 1
        else:
            for item in compressed:
                sub_counts = count_values(item)
                counts[0] += sub_counts[0]
                counts[1] += sub_counts[1]
        return counts
    
    return count_values(result)
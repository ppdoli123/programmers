def solution(s, skip, index):
    answer = ''
    alpha = 26
    for j in s :
        sk = index
        final = ord(j)
        while sk > 0 :
            if ord("z") < final + 1 :
                final -= 26
            if chr(final + 1) not in skip:
                sk -= 1
            final += 1
            
        answer += chr(final)
    return answer
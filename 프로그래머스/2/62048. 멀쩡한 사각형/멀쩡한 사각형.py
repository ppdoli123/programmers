def solution(w,h):
    answer = 0
    dimen = 1
    sum1 = 0
    while w%2 == 0 and h%2 == 0:
        w = int(w / 2)
        h = int(h / 2)
        dimen *= 2
        sum1 += dimen*w*h
    
    if w < h :
        for i in range(w):
            answer += int(i*h/w)
    else:
        for i in range(h):
            answer += int(i*w/h)
            
    return dimen*2*answer+sum1
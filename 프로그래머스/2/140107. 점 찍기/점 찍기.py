def solution(k, d):
    answer = 0
    Y = 0
    max_Y = int(d/k)
    X = k * max_Y
    ans = 0
    first = max_Y+1
    while Y <= d:
        while d*d - Y*Y < X*X or X > d:
            X -= k
            first -= 1
        Y += k
        answer += first
    return answer
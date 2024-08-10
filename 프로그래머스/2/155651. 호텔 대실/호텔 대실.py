def solution(book_time):
    #그니까 시간대가 겹치는 순간의 맥스값을 구하면 되는거잖아 ?
    # dp로 60*24
    dp = [0] * 25*60
    for i in book_time:
        start = i[0]
        exit = i[1]
        hour1,minute1 = start.split(':')
        hour2,minute2 = exit.split(':')
        for idx in range(int(hour1)*60+int(minute1),int(hour2)*60+int(minute2)+10):
            dp[idx] += 1
    answer = 0
    return max(dp)
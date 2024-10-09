def solution(m, musicinfos):
    result = []
    answer = '(None)'
    def replace_sharp(melody):
        return melody.replace('C#', 'h').replace('B#', 'q').replace('D#', 'i').replace('F#', 'j').replace('G#', 'k').replace('A#', 'l')
    max_time = 0
    for music in musicinfos:
        before,after,name,arkbo = music.split(",")
        af_hour,af_min = after.split(":") #끝나는 시간 분
        be_hour,be_min = before.split(":") #처음 시간 분
        time = (int(af_hour)*60+int(af_min))- (int(be_min) +int(be_hour)*60)
        # arkbo = ((time//len(ark)+1)*ark)[:time+1]
        
        arkbo = replace_sharp(arkbo)
        arkbo = arkbo * (time // len(arkbo)) + arkbo[0:time % len(arkbo)]
        m = replace_sharp(m)
        if m in arkbo and time > max_time:
            max_time = time
            answer = name

    return answer

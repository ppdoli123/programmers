#두개씩 저장
# 장르 > 노래 > 고유 번호 오름차순
def solution(genres, plays):
    answer = []
    volumn = {}
    sort_genre = {}
    for idx,genre in enumerate(genres):
        if genre not in volumn.keys():
            volumn[genre] = plays[idx]
            sort_genre[genre] = [idx]
        else :
            volumn[genre] += plays[idx]
            sort_genre[genre] += [idx]
    volumn = dict(sorted(volumn.items(), key=lambda x:x[1] ,reverse=True))
    for i in volumn.keys():
        tmp = []
        for j in sort_genre[i]:
            tmp.append([j,plays[j]])
        tmp = sorted(tmp , key=lambda x:x[1],reverse=True)
        if len(tmp) > 1:
            answer.append(tmp[0][0])
            answer.append(tmp[1][0])
        else:
            answer.append(tmp[0][0])
    return answer
def solution(today, terms, privacies):
    def today_s(year,month,day):
        return year * 28 * 12 + month * 28 + day
    answer = []
    terms_dic = {}
    for term in terms:
        product,month = term.split(" ")
        terms_dic[product] = month
    for i in range(len(privacies)):
        date,target = privacies[i].split(" ")
        year,mon,day = map(int,date.split("."))
        mon += int(terms_dic[target])
        if mon > 12:
            year += (mon//12)
            mon%=12
            
        if mon == 0:
            year -= 1
            mon = 12
        day -= 1
        today_year,today_mon,today_day = map(int,today.split("."))
        
        if today_s(today_year,today_mon,today_day) > today_s(year,mon,day):
            answer.append(i+1)
    return answer
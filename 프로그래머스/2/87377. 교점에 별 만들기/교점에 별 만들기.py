#자연수 교점을 다 찾기 ?
def solution(line):
    answer = []
    n = []
    for a,b,e in line:
        for c,d,f in line:
            if a*d - b*c == 0 :
                continue
            else:
                x = (b*f - e*d) /(a*d - b*c)
                y = (e*c - a*f) /(a*d - b*c)
                if x.is_integer() and y.is_integer() and [int(x),int(y)] not in n:
                    n.append([int(x),int(y)])
    #축에 평행인거
    print(n)
    n.sort(key=lambda x:x[0])
    min_x = n[0][0]
    max_x = n[-1][0]
    n.sort(key=lambda x:x[1])
    min_num = n[0][1]
    max_num = n[-1][1]
    print(min_x,max_x,min_num,max_num)
    result = [["." for i in range(max_x-min_x+1)] for _ in range(max_num-min_num+1) ]
    for i,j in n:
        result[j-min_num][i-min_x] = "*"
            

    result = result[::-1]
    for i in result:
        string = ""
        for j in i:
            string += j
        answer.append(string)
    return answer
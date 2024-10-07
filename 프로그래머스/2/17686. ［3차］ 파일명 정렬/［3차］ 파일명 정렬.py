def solution(files):
    answer = []
    #대소문자 구문
    #숫자 sort바로 하면 안되고 전체숫자로 솔트
    #숫자가 같을때는 입력 그대로 값 출력
    #헤드 넘버 테일을 짤라야됨
    numbers = []
    heads = []
    index = 0
    for i in files:
        name = ""
        num = ""
        name_bool = True
        for e in range(len(i)):
            
            if i[e] in "0123456789" :
                num += i[e]
                name_bool=False
            elif name_bool==True and i[e] not in "0123456789":
                name += i[e]
            elif name_bool==False and i[e] not in "0123456789":
                break
        heads.append([name.upper(),int(num),index])
        heads.sort(key=lambda x:(x[0],x[1]))
        index += 1
    for i in heads:
        answer.append(files[i[2]])
    print(heads)
        # a,b=i.split(num)
        # heads.append(a)
#         numbers.append(int(num))
#     files.sort(key=lambda x: (x[0].lower(), int(x[1])))
#     print(sorted(numbers))
#     head_idx = 0
#     for i in heads:
        
#         head_idx += 1
#     heads_so = sorted(heads)
#     id1 = []
#     for i in heads_so:
#         idx = 0
#         while True:
#             if heads[idx] == i and idx not in id1:
#                 id1.append(idx)
#                 break
#             idx += 1
    return answer
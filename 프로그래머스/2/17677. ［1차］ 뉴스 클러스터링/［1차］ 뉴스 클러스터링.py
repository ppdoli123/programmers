def solution(str1, str2):
    answer = 0
    bunza = 0
    bunmo = 0
    #모두 소문자로 바꾸고
    str1 = str.lower(str1)
    str2 = str.lower(str2)
    #두 글자 씩 뺴고
    arr_str1 = []
    arr_str2 = []
    i = 0
    e = 0
    while True:
        if i > len(str1)-2:
            break
        if str1[i] < "a" or str1[i] > "z":
            i += 1
            continue
        if str1[i+1] < "a" or str1[i+1] > "z":
            i += 1
            continue
        arr_str1.append(str1[i:i+2])
        i += 1

    while True:
        if e > len(str2)-2:
            break
        if str2[e] < "a" or str2[e] > "z":
            e += 1
            continue
        if str2[e+1] < "a" or str2[e+1] > "z":
            e += 1
            continue
        arr_str2.append(str2[e:e+2])
        e += 1
    #특수문자 빼고
    #비교
    ##공집합일때 1
    if len(arr_str1) == 0 and len(arr_str2) == 0 :
        return 65536
        
    dic_str1 = {}
    dic_str2 = {}
    
    for string in arr_str1: 
        # 코드를 작성하세요. 
        if string not in dic_str1: 
            dic_str1[string] = 1 
        else: 
            dic_str1[string] += 1 
            
    for string1 in arr_str2: 
        # 코드를 작성하세요. 
        if string1 not in dic_str2: 
            dic_str2[string1] = 1 
        else: 
            dic_str2[string1] += 1 
            
    for key in dic_str1.keys():
        if key in dic_str2.keys():
            bunza += min(dic_str1[key],dic_str2[key])
    
    bunmo = len(arr_str1) + len(arr_str2) - bunza
    
    return int(bunza/bunmo*65536)
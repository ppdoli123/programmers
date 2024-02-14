def solution(id_list, report, k):
    answer = []
    dicts = {}
    warn = {}
    report = set(report)
    for lists in report:
        answer.append(lists.split(" "))
        
    for keys in id_list:
        dicts[keys] = 0
            
    for keys in answer:
        if keys[1] not in warn:
            warn[keys[1]] = 1
            
        else:
            warn[keys[1]] += 1
        
        dicts[keys[0]] += 1
    
    for keys in answer:
        if warn[keys[1]] < k :
            dicts[keys[0]] -= 1

    return [value for value in dicts.values()]
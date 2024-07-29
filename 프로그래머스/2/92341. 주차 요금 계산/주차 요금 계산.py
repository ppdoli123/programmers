import math
def solution(fees, records):
    answer = []
    result_name=[]
    
    record = [i.split() for i in records] #2차원배열로 만들고
    
    for e in range(len(record)):
        if record[e][1] not in result_name:
            result_name.append(record[e][1])
    index = 0 #결과값에 해당되는 인덱스
    result = [0 for i in range(len(result_name))]
    result_name = sorted(result_name)
    for time,name,on in record:
        change = time.split(":")
        cor_time = int(change[0])*60+int(change[1])
        if on == 'IN':
            cor_name = name
            total_time = int(change[0])*60+int(change[1])
            result[result_name.index(cor_name)] -= total_time
        if on == "OUT":
            result[result_name.index(name)] += cor_time
    print(result)
    for idx in range(len(result)):
        if result[idx]<= 0 :
            result[idx] += ( 23*60 + 59 )
        
        if result[idx] <= fees[0]:
            result[idx] = fees[1]
        else:
            result[idx] = fees[1] + math.ceil((result[idx] - fees[0])/fees[2]) * fees[3]
    
    return result
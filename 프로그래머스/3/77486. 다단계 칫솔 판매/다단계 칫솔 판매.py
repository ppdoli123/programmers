def solution(enroll, referral, seller, amount):
    answer = []
    dic_idx = {}
    for idx,name in enumerate(enroll):
        dic_idx[name] = idx
    result = [0 for i in enroll]
    
    def dfs(name,price,result):
        tmp = int(dic_idx[name])
        name = referral[tmp]
        
        if price*0.1 < 1:
            result[tmp] += price
            return result
        else:
            result[tmp] += (price-int(price*0.1))
        if name != '-':
            price = int(price*0.1)
            dfs(name,price,result)
        else:
            return result
            
    for idx in range(len(seller)):
        name = seller[idx]
        price = amount[idx]*100
        dfs(name,price,result)
        
    return result
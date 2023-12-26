def solution(bandage, health, attacks):
    full = health
    i = 0
    time = 0
    for t in range(attacks[-1][0]+1):
        if t != attacks[i][0]:
            if health != full:
                health += bandage[1]
                if health > full:
                    health = full
                time += 1
                if time == bandage[0]:
                    health += bandage[2]
                    if health > full:
                        health = full
                    time = 0
        else:
            time = 0
            health -= attacks[i][1]
            if health <= 0 :
                return -1
            i+=1
        
    return health
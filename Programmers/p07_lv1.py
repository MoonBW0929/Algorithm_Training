def solution(bandage, health, attacks):
    
    time = 0
    bandage_cnt = 0
    c_health = health
    
    # 공격 받는 횟수 만큼 반복
    for attack in attacks:
        
        while True:
            time = time + 1
            
            # 공격 당할 경우
            if attack[0] == time:
                c_health = c_health - attack[1]
                bandage_cnt = 0
                break
            
            # 연속 성공 횟수 세기
            bandage_cnt = bandage_cnt + 1
            
            # 초당 회복
            c_health = c_health + bandage[1]
            
            # 최대 시전 시간 성공할 경우
            if bandage_cnt == bandage[0]:
                c_health = c_health + bandage[2]
                bandage_cnt = 0
                
            # 최대 체력을 넘기지 못함
            if c_health > health:
                c_health = health
        
        # 사망 했을 경우
        if c_health <= 0:
            c_health = -1
            break
    
    return c_health
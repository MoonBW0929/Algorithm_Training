def solution(friends, gifts):
    answer = 0 
    gift_cnt = {}
    next_gift = {}
    
    # 선물을 주고 받은 개수를 저장할 dictionary 생성
    for friend in friends:
        
        friends_dict = {}
        for f in friends:
            friends_dict[f] = 0
        
        gift_cnt[friend] = friends_dict
        next_gift[friend] = 0
    
    # 선물을 주고 받은 개수를 저장
    for gift in gifts:
        a, b = gift.split(" ")
        gift_cnt[a][b] = gift_cnt[a][b] + 1
    
    # 다음 달에 받을 선물 개수를 계산
    cnt = 0
    for now in friends:
        
        cnt = cnt + 1
        
        for i in range(cnt ,len(friends)):
            
            if gift_cnt[now][friends[i]] > gift_cnt[friends[i]][now]:
                next_gift[now] = next_gift[now] + 1
            elif gift_cnt[now][friends[i]] < gift_cnt[friends[i]][now]:
                next_gift[friends[i]] = next_gift[friends[i]] + 1
            else:
                
                a_total = 0
                b_total = 0
                for ff in friends:
                    a_total = a_total + gift_cnt[now][ff]
                    a_total = a_total - gift_cnt[ff][now]
                    b_total = b_total + gift_cnt[friends[i]][ff]
                    b_total = b_total - gift_cnt[ff][friends[i]]
                
                if a_total > b_total:
                    next_gift[now] = next_gift[now] + 1
                elif a_total < b_total:
                    next_gift[friends[i]] = next_gift[friends[i]] + 1
    
    # 가장 많은 선물 개수 구하기
    for ng in next_gift:
        if answer < next_gift[ng]:
            answer = next_gift[ng]
    
    return answer
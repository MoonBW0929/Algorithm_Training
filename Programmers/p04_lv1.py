def solution(wallet, bill):
    answer = 0
    
    # 지갑에 들어갈 수 있을 때까지 반복
    while True:
        # 지갑에 들어가는 지 확인
        if (wallet[0] >= bill[0] and wallet[1] >= bill[1]) or (wallet[0] >= bill[1] and wallet[1] >= bill[0]):
            break
        else:
            # 지폐 접기
            answer = answer + 1
            
            if bill[0] >= bill[1]:
                bill[0] = bill[0] // 2
            else:
                bill[1] = bill[1] // 2
        
    return answer
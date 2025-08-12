def solution(schedules, timelogs, startday):
    answer = len(schedules)
    empNum = 0
    limitTime = 0
    
    # 전체 직원 수로 검사
    for weekTime in timelogs:
        
        # 출근 해야되는 시간 구하기
        if (schedules[empNum] % 100) >= 50:
            limitTime = schedules[empNum] + 100 - 50
        else:
            limitTime = schedules[empNum] + 10
        
        dayCnt = startday
        
        # 각 직원 별 일주일 검사
        for dayTime in weekTime:

            # 토요일과 일요일은 제외
            if(dayCnt == 6) or (dayCnt == 7):
                dayCnt = (dayCnt % 7) + 1
                continue
            else:
                # 최대 출근 가능한 시간과 실제 출근한 시간을 비교
                if limitTime < dayTime:
                    answer = answer - 1
                    break
                
                dayCnt = (dayCnt % 7) + 1
        
        empNum = empNum + 1
            
    return answer
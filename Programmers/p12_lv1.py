def solution(park, routes):
    
    pos = []
    
    # 처음 시작 위치 탐색
    for i, line in enumerate(park):
        start = line.find("S")
        if start >= 0:
            pos = [i, start]
            break
    
    # 이동 명령 진행
    for route in routes:
        x = 0
        y = 0
        
        # 이동 방향 확인
        if route[0] == "E":
            x = 1
        elif route[0] == "W":
            x = -1
        elif route[0] == "N":
            y = -1
        elif route[0] == "S":
            y = 1
        
        # 명령 실행 후 공원 범위를 넘어가는 지 확인
        if (pos[0] + y*int(route[2])) < 0 or (pos[1] + x*int(route[2])) < 0:
            continue
        if (pos[0] + y*int(route[2])) >= len(park) or (pos[1] + x*int(route[2])) >= len(park[0]):
            continue
        
        # 이동 범위 내에 장애물이 있는 지 확인
        for i in range(1, int(route[2])+1):
            
            if park[pos[0] + y*i][pos[1] + x*i] == "X":
                break
                
            if i == int(route[2]):
                pos[0] += y*i
                pos[1] += x*i
    
    return pos
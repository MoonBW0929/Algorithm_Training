# 1x1씩 늘려가며 해당 위치에서 가능한 최대 정사각형의 사이즈 구하기
def check_regtangle(park, i, j):
    
    size = 1
    
    while True:
        
        # 최대 범위를 넘어갈 경우 break
        if (i + size >= len(park)) or (j + size >= len(park[0])):
            break
        
        if (park[i][j + size] == "-1") and (park[i + size][j] == "-1"):
            if park[i + size][j + size] == "-1":
                if size > 1:
                    cant = False
                    for k in range(1, size):
                        if not ((park[i + k][j + size] == "-1") and (park[i + size][j + k] == "-1")):
                            cant = True
                            break
                    if cant:
                        break
                    else : 
                        size = size + 1
                else:
                    size = 2
            else:
                break
        else:
            break
            
    return size

def solution(mats, park):
    
    answer = -1
    max_size = 1
    max_height = len(park)
    max_width = len(park[0])
    
    # 매트 크기가 큰 순서로 정렬
    mats.sort(reverse=True)
    
    # 들어갈 수 있는 가장 큰 정사각형의 크기 찾기
    for i, line in enumerate(park): 
        for j, block in enumerate(line):
            
            # 범위를 넘어가 굳이 계산할 필요 없는 경우 continue
            if (j >= (max_width - max_size)) or (i >= (max_height - max_size)):
                continue
            
            # 빈 블록을 찾으면 해당 위치에서 가능한 가장 큰 정사각형 구하기
            if block == "-1":
                size = check_regtangle(park, i, j)
                print((i, j))
                print(size)
                if max_size < size:
                    max_size = size
    
    # 들어갈 수 있는 가장 큰 매트 찾기
    for mat in mats:
        if max_size >= mat:
            answer = mat
            break
    
    return answer
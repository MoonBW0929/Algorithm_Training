def solution(name, yearning, photo):
    
    answer = []
    
    for pic in photo:

        sum = 0
        for man in pic:
            if man in name:
                sum = sum + yearning[name.index(man)]
        
        answer.append(sum)
    
    return answer
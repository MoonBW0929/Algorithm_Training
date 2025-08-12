def solution(n, w, num):
    answer = 0
    
    if (n % w) != 0:
        max_line = (n // w) + 1
    else:
        max_line = (n // w)
        
    line = (num - 1 + w) // w
    answer = max_line - line + 1
    
    if(line % 2) == 0:
        box_num = (num - w) - ((w * 2) * ((line - 1) // 2))
        box_num = w + 1 - box_num
    else:
        box_num = num - ((w * 2) * (line // 2))
        
    if (max_line % 2) == 0:
        if ((max_line * w) - n) >= box_num:
            answer = answer - 1
    else:
        if ((max_line * w) - n) >=  w + 1 - box_num:
            answer = answer - 1
    
    return answer

print(solution(20, 10, 17))
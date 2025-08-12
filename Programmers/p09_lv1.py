def solution(data, ext, val_ext, sort_by):
    
    answer = []
    
    cond = 0
    if ext == "date" : cond = 1
    elif ext == "maximum" : cond = 2
    elif ext == "remain" : cond = 3
    
    sort_cond = 0
    if sort_by == "date" : sort_cond = 1
    elif sort_by == "maximum" : sort_cond = 2
    elif sort_by == "remain" : sort_cond = 3
    
    for d in data:
        if d[cond] < val_ext:
            answer.append(d)
            
    answer.sort(key = lambda x : x[sort_cond], reverse = False)
    
    return answer
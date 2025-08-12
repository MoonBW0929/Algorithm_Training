def to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(":"))
    return minutes * 60 + seconds

def to_mmss(seconds):
    minutes = seconds // 60
    seconds = seconds % 60

    if minutes < 10: minutes = "0%d" % minutes
    else: minutes = str(minutes)
    if seconds < 10: seconds = "0%d" % seconds
    else: seconds = str(seconds)
    
    return minutes + ":" + seconds
    

def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = to_seconds(video_len)
    pos_sec = to_seconds(pos)
    op_start_sec = to_seconds(op_start)
    op_end_sec = to_seconds(op_end)

    # 처음 위치에서도 오프닝 건너뛰기 체크
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec

    for cmd in commands:
        if cmd == "prev":
            if pos_sec <= 10: pos_sec = 0
            else: pos_sec = pos_sec - 10
        elif cmd == "next":
            if pos_sec >= (video_len_sec - 10): pos_sec = video_len_sec
            else: pos_sec = pos_sec + 10

        # 오프닝 건너뛰기
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return to_mmss(pos_sec)
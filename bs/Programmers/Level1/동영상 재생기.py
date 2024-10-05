def solution(video_len, pos, op_start, op_end, commands):

    def change_minute(time):
        time = time.split(":")
        return (int(time[0]) * 60) + int(time[1])
    def check_opening(time):
        if op_start <= time <= op_end:
            return op_end
        else:
            return time

    video_len = change_minute(video_len)
    op_start = change_minute(op_start)
    op_end = change_minute(op_end)
    pos = change_minute(pos)
    # 시작값 오프닝 중이면 오프닝 끝으로 이동
    pos = check_opening(pos)
    for command in commands:
        if command == "prev":
            if pos < 10:
                pos = 0
            else:
                pos -= 10
        elif command == "next":
            if pos + 10 > video_len:
                pos = video_len
            else:
                pos += 10
        pos = check_opening(pos)
    res = []
    res.append(str(pos // 60).zfill(2))
    res.append(":")
    pos %= 60
    res.append(str(pos).zfill(2))

    return "".join(res)
def solution(book_time):

    time = [0 for i in range(60*24)]

    for start,end in book_time:
        start = 60 * int(start[:2]) + int(start[3:])
        end = 60 * int(end[:2]) + int(end[3:]) + 10
        if end > 1440:
            end = 1439
        for i in range(start,end):
            time[i] += 1
    return max(time)



print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))


def solution(a, b):
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]

    answer = (sum([months[i] for i in range(a - 1)]) + b - 1) % 7
    print(sum([months[i] for i in range(a - 1)]) + b - 1)
    return day[answer]

print(solution(5, 24))

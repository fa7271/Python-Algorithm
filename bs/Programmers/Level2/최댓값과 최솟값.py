def solution(s):
    num = list(map(int,s.split(" ")))
    return  min(num) + " " + max(num)
print(solution("-1 -2 -3 -4"))
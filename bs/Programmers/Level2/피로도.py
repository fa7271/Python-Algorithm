def solution(k, dungeons):
    dungeons.sort(key=lambda x:x[1])
    print(dungeons)

print(solution(80, [[80, 20], [50, 40], [30, 10]]))
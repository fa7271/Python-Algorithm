def solution(people, limit):
    count = 0
    start = 0
    end = len(people) -1
    people.sort()
    while start <= end:
        if people[start] + people[end] > limit:
            count +=1
            end -= 1
        else:
            count +=1
            start +=1
            end -= 1
    return count
print(solution([70, 50, 80, 50], 100))

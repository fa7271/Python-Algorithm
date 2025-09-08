
def solution(citations):
    for idx , people in enumerate(sorted(citations)):
        if people >= len(citations) - idx :
            return len(citations) - idx
    return 0

    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution([3, 0, 3,6, 1, 5]))

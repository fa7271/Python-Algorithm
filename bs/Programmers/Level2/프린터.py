def solution(priorities, location):
    list =  [(x,y) for x,y in enumerate(priorities)]
    answer = 0
    while True:
        now = list.pop(0) # 하나 빼줌
        if any(now[1] < list[1] for list in list): # now 가 리스트 안에 아무 값보다 크면
            list.append(now)    # 다시 집어넣어줌
        else:   # 아니면?
            answer += 1 # 그거 뺏으니깐 카운트 1 올려줌
            if now[0] == location: # 근데 now 가 나갈차례이면?
                return answer   # 그동안 카운트 리턴해줌

# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer


# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.
# print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1],0))


import heapq
def solution(operations):
    list = [] # heapq 만들예정 맨 위가 최솟값
    for i in operations:
        order, act = i.split(" ")
        if order == "I":
            heapq.heappush(list, int(act))
        else :
            if '-' in act: # - 가 붙으면 빼주는 것
                if len(list) == 0: # 근데 길이가 0 이면
                    pass    # 무시하고
                else:
                    heapq.heappop(list) # 길이가 0이 아니면 빼준다
            else: #최댓값을 삭제해줘야하는데 못함
                if len(list) == 0:
                    pass
                else:
                    list.remove(max(list))
                    heapq.heapify(list)

    return [max(list), min(list)] if len(list) >=2 else [0,0]



# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"] ))
print(solution( ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] ))

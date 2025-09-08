def solution(tickets):

    answer = []
    routes = dict() # 티켓 정보를 저장하는 딕셔너리

    for (start, end) in tickets:
        if start in routes:
            routes[start].append(end)
        else:
            routes[start] = [end]
    for i in routes.keys():
        routes[i].sort(reverse=True) # 뽑아야 하니깐 역순

    q = ["ICN"]
    while q:
        Top = q[-1]
        if (Top not in routes) or (not routes[Top]): # 더이상 방문할 곳이 없다 마지막 방문지점
            answer.append(q.pop())
        else:
            q.append(routes[Top].pop())

    return answer[::-1]



# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
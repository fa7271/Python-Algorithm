from collections import deque
def solution(menu, order, k):
    res = 0
    n = len(order)
    queue = deque()
    time = 0
    idx = 0
    while queue or idx < n:
        if not queue: # queue가 비어있으면
            time = (idx*k) +menu[order[idx]] # 끝나는 시간으로 time을 넣어주고
            idx += 1 # 다음 일 할 차례
        else:
            x = queue.popleft() # 할 일이 있으면
            time += menu[x] # 할일 끝나는 시간을 더해줌
        while idx < n and idx <= ((time-1) // k): # 밀린 주문을 넣어준다. time-1 // k를 해주 이전 시간 도착한 사람들의 idx를 처리해준다.
            queue.append(order[idx])
            idx +=1
        res = max(res,len(queue))
    return res+1
print(solution(	[5, 12, 30], [1, 2, 0, 1], 10))
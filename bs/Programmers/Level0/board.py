from collections import deque
def solution(num, total):
    if num ==1:
        return [total]
    deque_num = deque([i for i in range(num)])
    deque_num_sum = sum(deque_num)
    while deque_num_sum < total:
        x = deque_num.popleft()
        y = deque_num[-1] +1
        deque_num.append(y)
        deque_num_sum = deque_num_sum - x + y

    while deque_num_sum > total:
        x = deque_num.pop()
        y = deque_num[0]-1
        deque_num.appendleft(y)
        deque_num_sum = deque_num_sum - x + y

    return list(deque_num)



print(solution(4,5))
print(solution(1,5))
print(solution(3,12))
print(solution(5,15))



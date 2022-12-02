def dfs(numbers, target):

    first = [0]
    for i in numbers:
        lst = []
        for j in first:
            lst.append(j+i)
            lst.append(j-i)
        first = lst
    return first.count(target)
# print(dfs([1, 1, 1, 1, 1], 3))


from collections import deque
def bfs (numbers, target):
    res = 0
    q = deque()

    length = len(numbers)
    q.append([-numbers[0], 0])
    q.append([+numbers[0], 0])


    while q:
        num, i = q.popleft()
        if i+1 ==length:
            if target == num :
                res += 1
        else:
            q.append([num - numbers[i+1],i+1])
            q.append([num + numbers[i+1],i+1])

    return res


# print(bfs([1, 1, 1, 1, 1], 3))


def solution1(numbers, target):
    answer = dfs(numbers,target,0)
    return answer

def dfs(numbers,target, depth):

    answer = 0
    if len(numbers) == depth:
        if sum(numbers) == target:
            return 1
        else: return 0

    else:
        answer += dfs(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += dfs(numbers, target, depth+1)
        return answer

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer
print(solution1([1,1,1,1,1], 3))

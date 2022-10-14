

def solution(numbers, k):
    res = []
    if len(numbers) < 2 * k:
        x,y = divmod((2*k),len(numbers))
        res.append(numbers * x + numbers[:y] )
    res = sum(res,[])
    return res[2*k-2]

print(solution([1, 2, 3],3))
# print(solution(	1, 13, 1))

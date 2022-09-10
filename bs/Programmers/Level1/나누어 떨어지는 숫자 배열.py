def solution(arr, divisor):

    return [ i for i in sorted(arr) if i % divisor == 0 ] or [-1]

print(solution([5, 9, 7, 10],5))
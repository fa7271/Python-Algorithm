def solution(array):
    # array.count()
    return  ''.join(str(x) for x in array).count("7")

print(solution([7,17,77]))

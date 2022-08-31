# 피보나치 증명 1.
# def solution(x):
#     answer = 0
#     fib = [i for i in range(2)]
#     for i in range(2,x):
#         fib.append(fib[i-1]+fib[i-2])
#
#     print(fib)
#     print( fib[-1] )
#
# solution(2)


def solution(x):

    if x <=1:
        return x
    else:
        return solution(x-1) + solution(x-2)

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


# def solution(x):
#
#     if x <=1:
#         return x
#     else:
#         return solution(x-1) + solution(x-2)
#
# print(solution(2))


# top-down 방식
def fibo_dp(x):
    fib_array = [0,1]
    if x < len(fib_array):
        return fib_array[x]
    else:
        fib = fibo_dp(x-1) + fibo_dp(x-2)
        fib_array.append(fib)
        return fib

print(fibo_dp(7))


# bottom-up 방식
def fibo_dp_up(n):
    if n<=1 :
        return n
    fibo_array = [0,1]
    for i in range(2, n+1):
        top_down = fibo_array[i-1] + fibo_array[i-2]
        fibo_array.append(top_down)
    return fibo_array[n]
print(fibo_dp_up(7))

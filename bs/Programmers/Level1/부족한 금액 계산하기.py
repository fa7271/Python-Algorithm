def solution(price, money, count):
    res = sum([price * i for i in range(1,count+1)])  - money
    return res if res > 0 else 0

     # return [i for i in arr if i > min(arr)] or [-1]
print(solution(3, 20, 4))

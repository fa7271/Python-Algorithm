# 유클리드 호제법 사용하
def solution(x, y):
    max_xy = max(x, y)
    min_xy = min(x, y)
    res= []
    # 최대 공약수
    while y > 0:
        x, y = y, x % y


    res = [x, max_xy * min_xy//x]
    return res

# 입력 받은 수들을 최대공약수로 나눈수와 곱해주면 최소공배수를 출력할 수 있다.



print(solution(3,12))

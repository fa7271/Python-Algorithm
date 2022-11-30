def sosu(k):

    for i in range(2,int(int(k) ** 0.5)+1): # 소수찾기
        if int(k) % i== 0:
            return 0
    else:
        return 1
def solution(n, k):
    change_n = ""
    while n:            # 숫자를 k진법으로 변환
        change_n = str(n%k) +change_n
        n = (n//k)
    count = 0
    lst = change_n.split('0')
    for prime_number in lst:
        if len(prime_number) == 0 :
            continue
        if int(prime_number) < 2:
            continue
        count += sosu(int(prime_number))
    return count

    # if len(w)==0:    # 만약 0또는 1이거나 빈공간이라면 continue를 통해 건너뛴다.
    #     continue
    # if int(w)<2:
    #     continue



# print(solution(100,8))
# print(solution(437674,3))
# print(solution(110011,10))
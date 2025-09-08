def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

def solution(n, t, m, p): # 인원수에 맞춰서 진수 까지 변환함
    str =''
    now = 0
    while len(str) < t * m:
        str += convert(now,n)
        now +=1
    res =[]
    for i in range(p-1,len(str), m):
        res.append(str[i])

    return "".join(res)

# print(solution(16, 16, 2, 2))
print(solution(2,4,2,1))
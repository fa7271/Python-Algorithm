def solution(name, yearning, photo):
    dic = {x:y for x,y in zip(name,yearning)}
    res = []
    for i in range(len(photo)):
        result = 0
        for z in photo[i]:
            if z in dic:
                result += dic[z]

        res.append(result)
    return res


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
# print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))


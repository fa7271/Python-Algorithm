
def solution(record):
    res =[]
    dic = {}
    for records in record:
        i = records.split()
        if len(i) == 3:
            dic[i[1]] = i[2] # change 된거 까지 봐꿔줌
    for records in record:
        j = records.split()
        if j[0] == "Enter":
            res.append(dic[j[1]]+"님이 들어왔습니다.")
        elif j[0] == "Leave":
            res.append(dic[j[1]]+"님이 나갔습니다.")
    return res
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

# 이메일이 키값 아이디가 밸류값
# change 면 밸루깂 체인지



def solution(s):

    res = []
    split = 1

    while split < len(s):
        x= list(map(''.join, zip(*[iter(s)]*split)))
        count = 1
        result =''
        tmp =''

        for i in range(1,len(x)):
            if x[i] == x[i-1]:
                count += 1
            else:
                if count != 1:
                    result += str(count) + x[i]
                else:
                    result += x[i-1]

            print(result)
        res.append(result)
        if len(x) <= 1 :
            break
        split += 1

    # print(res)
# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))


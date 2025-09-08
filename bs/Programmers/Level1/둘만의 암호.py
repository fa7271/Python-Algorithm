def solution(s, skip, index):
    res = ''
    arr = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    for i in s:
        res += arr[(arr.index(i) + index) % len(arr)]
    return res


    list = []
    for i in s:
        count = 0
        for z in skip:
            if ord(i) <= ord(z) <= ord(i) + index:
                count += 1
        if ord(i)+count+index > 122:
            list.append(chr(ord(i)+count+index - 26))
        else :
            list.append(chr(ord(i)+count+index))
    return ''.join(list)
        # print(new_word)
        # if new_word >= 122:
        #     list.append(chr(new_word-26))
        # else:
        #     list.append(chr(new_word))
    # print(list)



print(solution("aukks", "wbqd", 5))
# 0 17 8 8 15
# 5 0 13 13 20
# a = 105 >> 110
# wbqd
# b = 106
# d = 108
# w = 111
# u = 117 ~ 122 // 119 ,98 113 100
# 97 ~ 121 122 > 97
# a b c d e f g h i j k l m n o p q r s t u w x y z
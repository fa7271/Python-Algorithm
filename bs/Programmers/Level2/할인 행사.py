def solution2(len_discount_number, want, number, discount) :
    want_dic = {i:0 for i in want}
    for want, count in zip(want_dic, number):
        want_dic[want] += count
    for i in discount[len_discount_number:len_discount_number+10]:
        if i in want_dic:
            want_dic[i] -= 1

    if any(want_dic.values()) != 0:
        return 0

    else: return 1


def solution(want, number, discount):
    if sum(number) > len(discount): # 할인진행기간보다 사고싶은게 많을경우
        return 0
    for i in want:      # 사려는 항목이 할인을 안 하는 경우
        if i not in discount:
            return 0

    len_discount_number = len(discount) - sum(number)
    ans = 0
    for i in range(len_discount_number+1):
        if solution2(i, want, number, discount) == 1:
            ans += 1
    return ans
    # while range != 0:
        # for i in discount[range:range+10]:
        #     if i in want_dic:
        #         want_dic[i] -= 1
        # if all(want_dic.values()) == 0:
        #     ans += 1
        # else:
        #     want_dic = {i : 0 for i in want}
        #     for want, count in zip(want_dic, number):
        #         want_dic[want] += count
        # solution2(range, want, number, discount)
        # range -= 1



print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
# print(solution(	["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
# 1. 숫자와 문자열 분리
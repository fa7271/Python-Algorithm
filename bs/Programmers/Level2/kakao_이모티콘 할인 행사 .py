from itertools import product
def solution(users, emoticons):

    res = [0, 0]
    for discounts in product((40,30,20,10), repeat = len(emoticons)):
        # print(discounts)
        result = [0, 0] # 이모티콘 판매액
        for user_discount, user_money in users:
            # print(user_discount,user_money)
            sub_pass = 0
            # print(discounts)
            for emoticon, discount in zip(emoticons,discounts):
                if discount >= user_discount:
                    sub_pass += emoticon * (1-discount/100)
            if sub_pass >= user_money:
                result[0] += 1
            else:
                result[1] += sub_pass
        res = max(res, result)
    return res
print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
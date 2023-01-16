from itertools import product
def solution(users, emoticons):

    res = [0, 0]
    for discounts in product((40,30,20,10), repeat = len(emoticons)):
        result = [0, 0] # 이모티콘 판매액
        for user_discount, user_money in users:
            sell = 0
            for emoticon, discount in zip(emoticons,discounts):
                print(emoticon,discount)
                if discount >= user_discount:
                    sell += emoticon * (1-discount/100)
            if sell >= user_money:
                result[0] += 1
            else:
                result[1] += sell
        res = max(res, result)
    return res
# 할인율 10%, 20%, 30%, 40%

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
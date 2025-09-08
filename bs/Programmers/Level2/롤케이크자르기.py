# # def solution(topping):
#     up_dic = dict()   # 형
#     down_dic = dict() # 동생
#     count = 0
#     for i in range(1,len(topping)):
#         for i in topping[:i]:
#             if i not in up_dic:
#                 up_dic[i] = 0
#             else:
#                 up_dic[i] += 1
#         for i in topping[i::]:
#             if i not in down_dic:
#                 down_dic[i] = 1
#             else:
#                 down_dic[i] += 1
#
#         if len(up_dic) == len(down_dic) :
#             count += 1
#     return count

# def solution(topping):
#     count = 0
#     for i in range(1, len(topping)):
#         if len(set(topping[:i])) == len(set(topping[i:])):
#             count += 1
#     return count

from collections import Counter
def solution(topping):
    main = Counter(topping)
    main_set = set()
    count = 0
    for i in topping:
        main[i] -= 1
        main_set.add(i)
        if main[i] == 0:
            main.pop(i)
        if len(main) == len(main_set) :
            count +=1
        if len(main) < len(main_set):
            break
    return count

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# print(solution([1, 2, 3, 1, 4]))

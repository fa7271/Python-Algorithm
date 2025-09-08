# def solution(k, d):
#     list = set()
#     angle = d**2
#     same_count = 0
#     for i in range(0,d,k):
#         for j in range(i,d+1,k):
#             if (i**2)+(j**2) <=angle:
#                 list.add((i,j))
#                 if i == j:
#                     same_count +=1
#
#     return len(list) * 2 - same_count

def soulution(k,d):
    count =0
    for i in range(0,d+1,k):
        y = (d**2) - (i**2)
        count += (int(y**0.5) // k) + 1

    return count
print(soulution(2,4))
# print(soulution(1,5))


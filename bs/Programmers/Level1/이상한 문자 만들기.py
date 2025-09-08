def solution(s):
        return ' '.join([''.join( [b.upper() if a % 2 == 0 else b.lower() for a, b in enumerate(i)] ) for i in s.split(' ')])
print(solution("try hello world"))

# def toWeirdCase(s):
#     liste = []
#     for i in s.split():
#         result = ''
#         for n,v in enumerate(i):
#             if n%2 == 0:
#                 result += v.upper()
#             else:
#                 result += v.lower()
#         liste.append(result)
#     return ' '.join(liste)
# #헤헤
# print("결과 : {}".format(toWeirdCase("try hello world")));
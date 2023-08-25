import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# word = list(sys.stdin.readline().rstrip())
#
# start = 0
# idx = 0
# while idx <len(word):
#     if word[idx] == "<": # 열린괄호이면
#         idx +=1
#         while word[idx] != ">": # 닫는 괄호 만날때까지
#             idx += 1 # 더해주고
#         idx += 1 # 그 다음 시작 하기 위해서 idx하나 더해줌
#     elif word[idx].isalnum(): # 숫자거나 알파벳이면
#         start = idx
#         while idx < len(word) and word[idx].isalnum(): # 범위보다 작고, 알파벳 숫자일때까지
#             idx += 1
#         temp = word[start:idx]
#         temp.reverse()
#         word[start:idx] = temp
#     else: # 공백인 경우
#         idx += 1
# print("".join(word))


text = input().replace('<', 'X<').replace('>', '>X')
tag_str = [t for t in text.split('X') if t]
results = []
for ts in tag_str:
    if '<' in ts and '>' in ts:
        results.append(ts)
    else:
        words = ts.split()
        reversed_words = [word[::-1] for word in words]
        results.append(' '.join(reversed_words))

print(''.join(results))
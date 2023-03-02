from collections import deque
def solution(begin, target, words):
    if target not in words:
        return -0

    Q = deque()
    Q.append([begin,0])
    print(Q)
    while Q:
        x, count = Q.popleft()

        if x == target:
            return count
        for i in range(len(words)):
            change = 0
            word = words[i]
            for j in range(len(x)):
                if x[j] != word[j]:
                    change+=1
            if change == 1:
                Q.append([word, count +1])
    return 0




print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
import heapq
def solution(n, k, enemy):
    list = []
    res = 0
    count = 0
    for i in enemy:
        res += i # 일단 막고봄
        if res <= n: #
            heapq.heappush(list,-i) # 일단 막고 보면서 막은 값들을 -붙여서 넣음 >> 밑에서 최댓 값 비교
            count += 1
        elif k > 0: # 이제 필살기를 써서 막을때
            k -= 1 # k를 1 깎고
            res += heapq.heappushpop(list,-i) # 가장 높은값과 에너미와 비교해서 높은거를 k를 막고 낮은거를 다시 집어넣은
            count +=1
        else:
            break
    return count
print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# print(solution(2, 4, [3, 3, 3, 3]))
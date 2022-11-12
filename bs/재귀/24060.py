import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

def merge_sort(list):
    n = len(list)

    if n <= 1:
        return list
    mid = (n+1)//2  # 중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(list[:mid]) # 재귀 호출로 첫 번째 그룹을 정렬  처음 부터 mid 까지
    g2 = merge_sort(list[mid:]) # 재귀 호출로 두 번째 그룹을 정렬  mid 부터 끝까지
    result, i, j =[], 0, 0
    while i < len(g1) and j < len(g2):  # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[i] < g2[j]: # 두 그룹의 맨 앞 자료 값을 비교
            result.append(g1[i])
            res.append(g1[i])
            i += 1
        else:
            result.append(g2[j])
            res.append(g2[j])
            j+=1
    while i < len(g1):
        result.append(g1[i])
        res.append(g1[i])
        i+=1
    while j < len(g2):
        result.append(g2[j])
        res.append(g2[j])
        j+=1
    return result

N, M = map(int,input().split())
arr = list(map(int,input().split()))
res = []

merge_sort(arr)
print(res[M-1]) if len(res) >= M else print(-1)


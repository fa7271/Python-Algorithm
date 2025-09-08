import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

def merge_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
    if n <= 1:
        return a
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2  # 중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(a[:mid]) # 재귀 호출로 첫 번째 그룹을 정렬  처음 부터 mid 까지
    g2 = merge_sort(a[mid:]) # 재귀 호출로 두 번째 그룹을 정렬  mid 부터 끝까지
    print(g1,g2)
# 두 그룹을 하나로 병합
    result = []
    # print(g1,g2,result)
    while g1 and g2:  # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]: # 두 그룹의 맨 앞 자료 값을 비교
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    # g1과 g2 중 이미 빈 것은 while을 바로 지나감
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    print('on',result)
    return result

d = [6, 8, 3, 9, 10, 12,15,13]
print(merge_sort(d))

# baeck 24060 참고

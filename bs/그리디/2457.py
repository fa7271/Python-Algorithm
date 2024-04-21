import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
n = int(input())

date = sorted([[sm * 100 + sd, em * 100 + ee] for sm, sd, em, ee in (map(int, input().split()) for _ in range(n))],
              key=lambda x: (x[0], x[1]))

count = 0
start = 301  # 301 ~ 1130
end = 0
while date:
    # 끝나는 날짜가 12월1일, 시작날짜가 3월1일 넘어가면 체크 안 해도 됨
    if start > 1130 or start < date[0][0]:
        break
    # date를 다 돌면서
    for i in range(len(date)):
        # 시작값인 안에 있는 값 보다 먼저 피어야함
        if start >= date[0][0]:
            # 기존에 있던것 보다 더 늦게 지면
            if end <= date[0][1]:
                # 더 늦게 지는걸로 바꿔줌
                end = date[0][1]
            # 꽃을 사용했으니 지워줌
            date.remove(date[0])
            # date[0][0] 이 크면 5월1일 에서 5월3일로 바뀌면 2일이 안 펴있으므로 안됨
        else:
            break
    #
    start = end
    count += 1
if start < 1201:
    print(0)
else:
    print(count)

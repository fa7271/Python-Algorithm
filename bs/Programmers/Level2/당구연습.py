def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        temp = []
        # 위쪽으로 부딪치기
        if not (startX == x and y > startY):
            temp.append(abs(x - startX) ** 2 + abs(2 * n - y - startY) ** 2)
        # 아래로 부딪치기
        if not (startX == x and y < startY):
            temp.append(abs(x - startX) ** 2 + abs(y + startY) ** 2)
        # 왼쪽으로 부딪치기
        if not (startY == y and x < startX):
            temp.append(abs(x + startX) ** 2 + abs(y - startY) ** 2)
        #  오른쪽
        if not (startY == y and x > startX):
            temp.append(abs(2 * m - startX - x) ** 2 + abs(y - startY) ** 2)
        answer.append(min(temp))
    return answer


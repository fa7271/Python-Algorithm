import numpy


def solution(rows, columns, queries):
    graph = [[i + j for j in range(1, columns + 1)] for i in range(0, rows * columns, columns)]
    answer = []
    for x1, y1, x2, y2 in queries:
        start = graph[x1 - 1][y1 - 1]
        res = start

        # 왼쪽 세로
        for x in range(x1 - 1, x2 - 1):
            temp = graph[x + 1][y1 - 1]
            graph[x][y1 - 1] = temp
            res = min(temp, res)
        print(numpy.array(graph))
        # 밑에 가로
        for x in range(y1 - 1, y2 - 1):
            temp = graph[x2 - 1][x + 1]
            graph[x2 - 1][x] = temp
            res = min(temp, res)
        print(numpy.array(graph))
        # 오른쪽 세로
        for k in range(x2 - 1, x1 - 1, -1):
            temp = graph[k - 1][y2 - 1]
            graph[k][y2 - 1] = temp
            res = min(res, temp)
        print(numpy.array(graph))
        # 위에 가로
        for k in range(y2 - 1, y1 - 1, -1):
            temp = graph[x1 - 1][k - 1]
            graph[x1 - 1][k] = temp
            res = min(res, temp)
        graph[x1 - 1][y1] = start
        print(numpy.array(graph))
        answer.append(res)
        break
    print(answer)


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))

import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

def solution(s):
    string = ['#']
    for i in range(len(s)):
        string.append(s[i])
        string.append('#')
    # 홀 수 갯수로 만들어준다.
    answer = manachers(string, len(string))
    return answer


def manachers(S, N):
    A = [0] * N
    # 확정된 오른쪽 끝과, 중심
    r, p = 0, 0
    for i in range(N):  #
        if i <= r:
            # i의 대칭점 찾기 / r-i: 자신이 속한 팰린드롬까지의 길이
            A[i] = min(A[2 * p - i], r - i)
        while i - A[i] - 1 >= 0 and i + A[i] + 1 < N and S[i - A[i] - 1] == S[i + A[i] + 1]:
            A[i] += 1
        #  팰린드롬의 오른쪽 끝이 현재까지 발견된 가장 큰 팰린드롬의 오른쪽 끝보다 더 오른쪽에 있는지 확인
        #  맞다면 오른쪽 중심 바꿔주고, 시작지점 바꿔준다.
        # print("시작점 i:" , i, "중심 p:", p, "오른쪾 r:", r,"대칭점 :", "A[i] :",A[i])
        if r < i + A[i]:
            r = i + A[i]
            p = i
    return max(A)

print(solution(input()))

# 이전에 구했던 회문 중 가장 오른쪽으로 긴 회문의 중심 인덱스 p
# 와 오른쪽 끝 인덱스인 r
# 값을 통해 이전에 구한 데이터를 활용하여 연산을 최적화한다.

# https://ialy1595.github.io/post/manacher/
# https://m.blog.naver.com/jqkt15/222108415284
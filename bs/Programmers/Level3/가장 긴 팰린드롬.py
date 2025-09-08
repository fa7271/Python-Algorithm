def solution(s):
    lst = []  # 팰린드롬 부분 문자열의 길이를 저장할 리스트
    Max = 0  # 가장 긴 팰린드롬 부분 문자열의 길이를 저장할 변수

    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:  # 현재 부분 문자열이 팰린드롬인지 확인
                Max = max(Max, len(s[i:j]))  # 가장 긴 팰린드롬 부분 문자열의 길이 갱신

    return Max  # 가장 긴 팰린드롬 부분 문자열의 길이 반환
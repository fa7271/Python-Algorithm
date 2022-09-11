파이썬 기술  1, 컴프리핸션 잘 이해하기 (리스트 딕셔너리)

# return [sorted(array[a-1:b])[c-1] for a,b,c in commands]

# 이중 리스트 [ [] ] 일때 [] 하나 빼고 출력하기 print(*) * 하고 출력하면됨

# combination = list(itertools.combinations(nums, 3)) # 리스트 num 에서 3개 뽑느 수열

#''.join(리스트)''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수인 것입니다.
# ex
# def solution(n):
#     return int("".join(list(reversed(sorted(str(n))))))
# print(solution(118372))

#     return s.isnumeric() 숫자이면 true 문자열이면 false 리턴

# divmod() : 몫과 나머지를 같이 반환해주는 함수
# 2) int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌
# ex) 3진법 뒤집기 프로그래머스

tmp = bin(arr1[i] or arr2[i])
or / | 차이 | 은 이진수를 반환함
tmp = tmp[2:].zfill(n)
# 앞에 두개 짜르고 뒤에 n 자릿수 만큼만큼 0 차운다
파이썬 기술  1, 컴프리핸션 잘 이해하기 (리스트 딕셔너리)

# return [sorted(array[a-1:b])[c-1] for a,b,c in commands]

# 이중 리스트 [ [] ] 일때 [] 하나 빼고 출력하기 print(*) * 하고 출력하면됨

# combination = list(itertools.combinations(nums, 3)) # 리스트 num 에서 3개 뽑느 수열
# for i in product(l1,l2,repeat=1): #l1과 l2의 모든 쌍을 지어 리턴한다

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
앞에 두개 짜르고 뒤에 n 자릿수 만큼만큼 0 차운다


return sorted(sorted(strings), key=itemgetter(n))
# itemgetter(n) 은 sorted() 함수의 key 매개변수에 사용 가능 튜플, 딕셔너리 에서도 사용 가능

res = new_id.lower() # 1. 소문자
res = ''.join(re.compile('[0-9a-z_.\-]+').findall(res)) # 2. 문자제거
res = re.sub('\.\.+' , '.' , res) # 3. 점 2개 짜리 1개로 바꿈
res = res.strip('.') # 4. 양쪽 끝 . 제거 strip() 매개변수로 넘겨주는거 문자열 시작/ 끝에서 제거해줌

s = bin(len(s))[2:] # 2진 변환 bin(숫자)  # [2:] 해줘야 첫 0b 빼고 출력

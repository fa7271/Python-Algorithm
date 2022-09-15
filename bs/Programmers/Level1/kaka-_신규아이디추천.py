import re
def solution(new_id):



    res = new_id.lower() # 1. 소문자

    res = ''.join(re.compile('[0-9a-z_.\-]+').findall(res)) # 2. 문자제거

    res = re.sub('\.\.+' , '.' , res) # 3. 점 2개 짜리 1개로 바꿈

    res = res.strip('.') # 4. 양쪽 끝 . 제거 strip() 매개변수로 넘겨주는거 문자열 시작/ 끝에서 제거해줌

    if res =='':
        res +='a'

    if len(res)>=16:
        res = res[:15]
        res = res.rstrip('.') # 6. 우측 '.' 제거

    if len(res) < 3:
        res = res + res[-1] * (3-len(res))

    return res

print(solution("...!@BaT#*..y.abcdefghijklm" ))
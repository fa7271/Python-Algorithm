
def solution(m, musicinfos):
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    res = []
    for i in range(len(musicinfos)):
        time1, time2, name, code = musicinfos[i].split(",")
        Min = int(time2[3::]) - int(time1[3::])
        hour = int(time2[0:2]) - int(time1[0:2])
        dif = (hour*60) + Min
        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        res.append([dif, name, code])
    res.sort(key=lambda x:-x[0])
    for i in range(len(musicinfos)):
        a, b = divmod(res[i][0],len(res[i][2]))
        print(a,b)
        full = res[i][2] * a + res[i][2][:b]
        print(full)
        if m in full:
            return res[i][1]
    else:
        return'(None)'

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
#
# 먼저 입력값 m 의 샾붙은것들을 치환해준다
#
# 포문을 돌면서 dif 음악재생시간을 구해주고 노래코드구성을 치환을 해주면서
# res에 재생시간, 노래제목, 코드구성을 넣어주고
# 재생시간 긴 순으로 sort해줌
#
# 정렬된 res 가지고
# for문 돌면서 몫과 나머지를 이용하여 코드구성을 다 만듦
# 그리고 if 문 없으면 none


# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
# 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
# def shap_to_lower(s):  # 샵이 포함된 음을 소문자로 변경
#     s = s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
#     return s
#
#
# def solution(m, musicinfos):
#     data = []
#     m = shap_to_lower(m)
#     for i in musicinfos:
#         i = i.split(',')
#         data.append([
#             int(i[1][:2]) * 60 + int(i[1][3:]) - (int(i[0][:2]) * 60 + int(i[0][3:])),  # 재생시간
#             i[2],  # 제목
#             shap_to_lower(i[3])])  # 멜로디
#     print(data)
#     data.sort(key=lambda x: (-x[0]))  # 재생시간 긴 순으로 정렬
# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

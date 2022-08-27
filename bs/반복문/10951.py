import sys
sys.stdin = open('/Python/h.txt', 'r')

for i in sys.stdin:
    a, b = map(int,i.split())
    print(a+b)


# input vs sys.stdin
#
# input은 Python 공식 문서에 따르면
#
# promt 인자가 있을 경우 끝에 개행 문자를 붙이지 않고 표준 출력에 쓴다. 그 후 함수는 입력을 통해 한 줄을 읽고, 문자열로 변환하여(그 이후  줄 바꿈을 제거) 값을 반환한다.
#
# input ->개행문자를 벗겨 내어 -> 문자열로 변환 ->  줄 바꿈 제거 -> return
#
# sys.stdin 은
#
# stdin은 모든 대화형 입력에 사용된다.(input()호출을 포함)
#
# sys.stdin 은 여러줄을 입력받을때
# sys.stdin.readline() - 한 줄 입력
# sys.stdin.readline() 사용한 여러줄 입력
#
# 속도 면에서는 input 보다 sys.stdin이 빠르다
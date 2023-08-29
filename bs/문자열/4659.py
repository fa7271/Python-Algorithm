import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
import re
while True:
    N = sys.stdin.readline().rstrip()
    lst = ["a","e","i","o","u"]
    if N == "end":
        break

    check_1 = False
    check_2 = True
    check_3 = True
    for i in range(len(N)):
        if N[i] in lst:
            check_1 = True
        if i > 0:
            if N[i] == N[i-1] and N[i-1] != "e" and N[i-1] != "o":
                check_3 = False
        if i > 1:
            if N[i-2] in lst and N[i-1] in lst and N[i] in lst:
                check_2 = False
            if N[i-2] not in lst and N[i-1] not in lst and N[i] not in lst:
                check_2 = False

    if check_1 and check_2 and check_3:
        print("<" + N + "> is acceptable.")
    else:
        print("<" + N + "> is not acceptable.")






# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
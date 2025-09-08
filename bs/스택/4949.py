import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

while True:
    s = input()
    if s == '.':
        break
    st = []
    for i in s:
        if i not in '()[]':
            continue
        if i == '(' or i == '[':
            st.append(i)
        elif (i == ')' and st and st[-1] == '(') or (i == ']' and st and st[-1] == '['):
            st.pop()
        else:
            st.append(0)
            break
    print('no' if st else 'yes')
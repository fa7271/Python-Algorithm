import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


count = 0
res = 0
for i in range(20):
    count += 1
    sub, num, grade = input().split(" ")
    if grade == "Pass":
        count -= 1
    elif grade =="F":
        res +=float(0)
    else:
        res += float(num)
print(res/count)




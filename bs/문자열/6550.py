import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

while True:
    try:
        A, B = sys.stdin.readline().rstrip().split()

        count = 0
        for i in B:
            if count < len(A) and A[count] == i:
                count += 1

        if count == len(A):
            print("Yes")
        else:
            print("No")
    except:
        break

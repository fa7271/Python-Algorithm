import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

def cantor(arr,N):
    if N == 1:
        return
    for i in range(arr + N//3, arr + (N//3)*2):
        res[i] = " "
    cantor(arr, N//3)
    cantor(arr+ N//3 * 2 , N//3)
while True:
    try :
        N = int(sys.stdin.readline())
        res = ['-'] * (3**N)
        cantor(0, 3**N)
        print("".join(res))
    except:
        break


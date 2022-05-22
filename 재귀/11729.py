import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')



def hanoi(N,i,j,via):                  # i 시작 j 목표 via 보조
    if N == 1:
        print(i,j)
        return
    else:
        hanoi(N-1,i,via,j)
        print(i,j)
        hanoi(N-1,via,j,i)

N = int(input())
print(2**N-1)
hanoi(N,1,3,2)

# hanoi(2, ‘A’, ‘B’, ‘C’) : start에서 3번까지
# 3번 원반을 ‘C’로 옮기기 위해서는 먼저 위의 두 원반을 ‘B’로 옮겨야 한다.
# 이후 3번 원반을 ‘C’로 옮긴다 : 4번
# hanoi(2, ‘B’, ‘C’, ‘A’) : 5번 ~
# 3번을 ‘C’로 옮긴 후 ‘B’에 있는 두 개의 원반을 ‘C’로 옮긴다. 이때 ‘A’를 경유한다.


# hanoi(3,1,3,2)
#     hanoi(2,1,2,3)
#         hanoi(1,1,3,2)
#         hanoi(1,3,2,1)
#     hanoi(2,2,3,1)
#         hanoi(1,2,1,3)
#         hanoi(1,1,3,2)

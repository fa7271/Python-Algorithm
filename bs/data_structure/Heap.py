class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)

        i = len(self.data)-1

        while self.data[i//2]: # 부모가 있으면
            if self.data[i//2] < self.data[i]: # 자식이 부모보다 크면
                self.data[i//2], self.data[i] = self.data[i], self.data[i//2] # 바꿔저장하고
                i = i//2 # 위로 한번 더 올라감
            else: # 알맞게 감
                break


def solution(x):
    return 0


# [0,24,12,18,21,8,6,4,2]
# i 는 10 마지막 30
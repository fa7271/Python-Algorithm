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
    def remove(self):
        # 하나이상의 노드가 존재하는 경우
        if len(self.data) > 1:
            # 맨마지막 원소와 위치바꾸기
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data


    def maxHeapify(self, i):
        # i는 어느 기준으로 바꿀건가

        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = i * 2
        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = i * 2 + 1
        greatest = i

        # 자신(i), 왼쪽자식(left), 오른쪽자식(right) 중 최대를 찾아서 이것의 인덱스를 smallest에 담는다
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if left < len(self.data) and self.data[left] > self.data[greatest]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            greatest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if right < len(self.data) and self.data[right] > self.data[greatest]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            greatest = right

        # 만약 이 인덱스가 i와 같지 않다면 자식들 중에 나보다 큰 키값을 가진 노드가 발견된 경우
        if greatest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[greatest] = self.data[greatest], self.data[i]
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(greatest)
def solution(x):
    return 0


# [0,24,12,18,21,8,6,4,2]
# i 는 10 마지막 30
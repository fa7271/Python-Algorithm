

def solution(arr,target):
    left , right = 0, len(arr)-1
    arr.sort()
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target: # 찾고자 하는 값이 중간값보다 작음
            right = mid -1
        else:
            left = mid+1
    return -1






print(solution([1,6,2,2,3,7,5,10,2],6))
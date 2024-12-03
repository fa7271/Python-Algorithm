class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1 = [i for i in nums1 if i != 0]
        nums1.extend(nums2)
        nums1 = nums1.sort()
        return nums1

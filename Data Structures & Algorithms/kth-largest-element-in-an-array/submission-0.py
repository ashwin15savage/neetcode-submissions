class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        i=n-k
        return nums[i]
        
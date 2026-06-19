class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a={}
        for i,num in enumerate(numbers):
            diff=target-num
            if diff in a:
                a[diff]+=1
                i+=1
                return [a[diff],i]
            a[num]=i
        return []

        
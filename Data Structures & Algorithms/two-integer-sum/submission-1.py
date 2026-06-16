class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A=[]

        for i,num in enumerate(nums):
            A.append([num,i])

        i,j=0,len(nums)-1

        A.sort()

        while i<j:
            cur=A[i][0]+A[j][0]

            if cur==target:
                return [min(A[i][1], A[j][1]),
                max(A[i][1], A[j][1])]

            elif cur<target:
                i=i+1

            else:
                j=j-1
        return[]

         

        
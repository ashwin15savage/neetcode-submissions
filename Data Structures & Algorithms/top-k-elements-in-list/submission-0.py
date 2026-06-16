class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        d={}

        for i in nums:
            d[i]=1+d.get(i,0)

        heap=[]

        for num,key in d.items():
            heapq.heappush(heap,(key,num))

            if len(heap)>k:
                heapq.heappop(heap)

        l=[]
        for freq,num in heap:
            l.append(num)

        return l

        
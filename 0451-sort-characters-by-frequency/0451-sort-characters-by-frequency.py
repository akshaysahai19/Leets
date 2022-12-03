class Solution:
    def frequencySort(self, s: str) -> str:

        freqMap = {}
        for l in s:
            if l not in freqMap:
                freqMap[l]=(1, l)
            else:
                freqMap[l]=(freqMap[l][0]+1, l)
        
        values = []
        for k,v in freqMap.items():
            heapq.heappush(values, (-v[0], v[1]))

        ans = ''
        while values:
            c,l = heapq.heappop(values)
            while c<0:
                ans+=l
                c+=1


        return ans
        

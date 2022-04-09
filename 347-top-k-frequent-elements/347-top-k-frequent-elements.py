class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in nums:
            if i in count_map:
                count_map[i]+=1
            else:
                count_map[i] = 1
        
        x = dict(sorted(count_map.items(), key=lambda item: item[1]))
        keys = list(x.keys())
        return keys[len(keys)-k:len(keys)]
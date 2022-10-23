class Solution:
    def maximumGap(self, arr: List[int]) -> int:

        if len(arr)<2:
                return 0

        bucketSize = len(arr)
        bucket = [[float('-inf')]]*(bucketSize)
        minVal = min(arr)
        maxVal = max(arr)
        
        if minVal==maxVal:
            return 0

        bucketMinMax = [[float('inf'),float('-inf')] for i in range(bucketSize)]
        for i in range(len(arr)):
            bucketIndex = int((arr[i]-minVal)*(bucketSize-1)//(maxVal-minVal))
            bucketMinMax[bucketIndex][0] = min(bucketMinMax[bucketIndex][0], arr[i])
            bucketMinMax[bucketIndex][1] = max(bucketMinMax[bucketIndex][1], arr[i])
            if bucket[bucketIndex][0]!=float('-inf'):
                bucket[bucketIndex].append(arr[i])
            else:
                bucket[bucketIndex] = [arr[i]]
        stack = bucketMinMax[0]
        result = 0
        for i in range(1, len(bucketMinMax)):
            if stack[0]!=float('-inf') and bucketMinMax[i][0]!=float('inf'):
                result = max(result, bucketMinMax[i][0]-stack[1])
                stack = bucketMinMax[i]

        return result
        
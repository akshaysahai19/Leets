class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals, key=lambda x: x[0])
        # print(sortedIntervals)
        
        if len(sortedIntervals)==0:
            return []
        
        result = [sortedIntervals[0]] 
        print(result)
        index = 1
        
        while index<len(sortedIntervals):
            lastInterval = result[len(result)-1]
            currentInterval = sortedIntervals[index]
            if lastInterval[1]>=currentInterval[0]:
                if lastInterval[1]<currentInterval[1]:
                    result[len(result)-1][1] = currentInterval[1]
                index+=1
            else:
                result.append(currentInterval)
                index+=1
        return result
                
        
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
            print('length = ', len(lastInterval))
            print('Val = ', lastInterval)
            if lastInterval[1]>=currentInterval[0]:
                if lastInterval[1]<currentInterval[1]:
                    result[len(result)-1][1] = currentInterval[1]
                    index+=1
                else:
                    index+=1
            else:
                result.append(currentInterval)
                index+=1
        return result
                    
        
#         while index<len(sortedIntervals)-1:
#             currentInterval = sortedIntervals[index]
#             nextInterval = sortedIntervals[index+1]
#             newInterval = [currentInterval[0]]
#             if currentInterval[1]>=nextInterval[0]:
#                 if currentInterval[1]>=nextInterval[1]:
#                     newInterval.append(currentInterval[1])
#                 else:
#                     newInterval.append(nextInterval[1])
                    
#                 index+=2
#             else:
#                 newInterval.append(currentInterval[1])
#                 index+=1
                
#             result.append(newInterval)
               
#             if index==len(sortedIntervals)-1:
#                 if newInterval[1]>sortedIntervals[index][0]:
#                     if newInterval[1] < sortedIntervals[index][1]:
#                         newInterval[1] = sortedIntervals[index][1]
#                         result.append(newInterval)
#                     else:
#                         newInterval = [sortedIntervals[index][0], sortedIntervals[index][1]]
#                         result.append(newInterval)
        
        return result
                
        
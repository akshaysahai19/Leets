class Solution(object):
    
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        temp = {}
        for x in allowed:
            if x not in temp.keys():
                temp[x] = 1
        
        global_count = 0
        for w in words:
            present = True
            for l in w:
                if l not in temp.keys():
                    present=False
            if present:
                global_count+=1
        
        return global_count
        
        
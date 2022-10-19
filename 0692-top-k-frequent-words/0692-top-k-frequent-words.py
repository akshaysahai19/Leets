class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        countDict = {}
        for word in words:
            if word in countDict:
                countDict[word]+=1
            else:
                countDict[word] = 1
        
        words = set(words)
        
        word_list = []
        for w in words:
            word_list.append([countDict[w],w])
        print(word_list)
        
        word_list = sorted(word_list, key = lambda x:(-x[0],x[1]), reverse=False)
        print(word_list)
        
        res = []
        for wl in word_list[:k]:
            res.append(wl[1])
        return res
        
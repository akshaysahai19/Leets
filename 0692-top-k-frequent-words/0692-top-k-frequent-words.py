class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        countDict = {}
        for word in words:
            if word in countDict:
                countDict[word]+=1
            else:
                countDict[word] = 1
        
        word_list = []
        for w in set(words):
            word_list.append([countDict[w],w])
        
        word_list = sorted(word_list, key = lambda x:(-x[0],x[1]), reverse=False)
        
        res = []
        for wl in word_list[:k]:
            res.append(wl[1])
        return res
        
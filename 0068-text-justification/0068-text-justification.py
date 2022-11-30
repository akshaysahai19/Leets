class Solution:
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        totalLen = len(words[0])
        currString = words[0]
        currWordsLen = len(words[0])
        res = []
        
#         function to seggregate words based on spaces
        for i in range(1, len(words)):
            word = words[i]
            nextLen = totalLen+1+len(word)
            if nextLen<=maxWidth:
                totalLen=nextLen
                currWordsLen+=len(word)
                currString = currString + ' ' + word
            else:
                res.append([currString, currWordsLen])
                totalLen = len(word)
                currWordsLen = totalLen
                currString = word
                
        res.append([currString, currWordsLen])
        
        
#         function to add spaces on each of the lines in res
        ans = []
        for i, line in enumerate(res):
            words = line[0].split(' ')
            spaceCount = len(words)-1
            
            currString = ''
#             if else if line contains just 1 word or if it's the last line
            if len(words)==1 or i==len(res)-1:
                currString = ' '.join(words)
                currString+= ' '*(maxWidth-len(currString))
            else:
#                 this creates a list of spaces that needs to be added after ith word
                spaces = []
                rem = maxWidth-line[1]
                for i in range(spaceCount):
                    spaces.append(rem//spaceCount)
                    spaces[i] += 1 if i < rem%spaceCount else 0
                spaces.append(0)
                
                for i, word in enumerate(words):
                    currString = currString+word+' '*spaces[i]
                        
            ans.append(currString)
                
        return ans
                
                
        
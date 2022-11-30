class Solution:
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        lenMap = {}
        for word in words:
            lenMap[word]=len(word)
        
        totalLen = len(words[0])
        currString = words[0]
        currWordsLen = len(words[0])
        res = []
        
        for i in range(1, len(words)):
            word = words[i]
            nextLen = totalLen+1+lenMap[word]
            if nextLen<=maxWidth:
                totalLen=nextLen
                currWordsLen+=lenMap[word]
                currString = currString + ' ' + word
            else:
                res.append([currString, currWordsLen])
                totalLen = lenMap[word]
                currWordsLen = totalLen
                currString = word
                
        res.append([currString, currWordsLen])
        
        
        ans = []
        for i, line in enumerate(res):
            currString = ''
            words = line[0].split(' ')
            # space = 0
            spaceCount = len(words)-1
            rem = maxWidth-line[1]
            # if len(words)>1:
            #     space = (maxWidth-line[1])//(len(words)-1)
            #     rem = (maxWidth-line[1]) - space*(len(words)-1)
            # else:
            #     rem = (maxWidth-line[1])
            # print('space = ', space)
            # print('rem = ', rem)
            
            currString = ''
            if len(words)==1 or i==len(res)-1:
                currString = ' '.join(words)
                currString+= ' '*(maxWidth-len(currString))
                print('00 = ', currString)
            else:
                spaces = []
                for i in range(spaceCount):
                    spaces.append(rem//spaceCount)
                    spaces[i] += 1 if i < rem%spaceCount else 0
                spaces.append(0)
                print('spaces = ', spaces)
                
                for i, word in enumerate(words):
                    currString = currString+word+' '*spaces[i]
                print('11 = ', currString)
                        
            ans.append(currString)
                
                
        
        print(res)
        print(ans)
        
        return ans
                
                
        
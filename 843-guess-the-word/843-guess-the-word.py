# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        wordList = set(wordlist)
        guesses = 0
        
        while wordList and guesses<10:
            guessWord = wordList.pop()
            matchVal = master.guess(guessWord)
            newList = []
            for item in wordList:
                count=0
                for i in range(6):
                    if item[i]==guessWord[i]:
                        count+=1
                if count==matchVal:
                    newList.append(item)
            wordList = set(newList)
                    
                    
                    
        
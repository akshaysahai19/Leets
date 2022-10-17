class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        if len(set(list(sentence)))==26:
            return True
        return False
        
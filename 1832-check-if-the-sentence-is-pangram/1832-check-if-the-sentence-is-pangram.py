class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = dict.fromkeys(string.ascii_lowercase, 0).keys()
        alphabets = ''.join(list(alphabets))
        
        sentence = set(list(sentence))
        sentence = ''.join(sorted(sentence))
        
        if alphabets==sentence:
            return True
        return False
        
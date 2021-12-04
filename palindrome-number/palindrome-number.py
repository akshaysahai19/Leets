class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        j = len(x)-1
        for i in range(len(x)):
            if(x[i]==x[j]):
                j-=1
            else:
                return False;
        return True
            
        
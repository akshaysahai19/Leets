class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if(len(asteroids)==0 or len(asteroids)==1):
            return asteroids
        
        i = len(asteroids)-1
        while(i>=0):
            # print('current i = ',i)
            if(i==0):
                break
            if(asteroids[i]<0):
                if(asteroids[i-1]>=0):
                    if(abs(asteroids[i])>asteroids[i-1]):
                        asteroids.pop(i-1)
                        i-=1
                    elif (abs(asteroids[i])<asteroids[i-1]):
                        asteroids.pop(i)
                        i=len(asteroids)-1
                    else:
                        asteroids.pop(i)
                        asteroids.pop(i-1)
                        i=len(asteroids)-1
                else:
                    i-=1
            else:
                i-=1 
                        
        return asteroids
            
        
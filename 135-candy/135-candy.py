class Solution:
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings)
        candiesLeft = [1]*(size)
        candiesRight = [1]*(size)
        
        for j in range(1, len(ratings)):
            if ratings[j]>ratings[j-1]:
                candiesLeft[j] = candiesLeft[j-1]+1

        for j in range(len(ratings)-2, -1, -1):
            if ratings[j]>ratings[j+1]:
                candiesRight[j] = candiesRight[j+1]+1
        
        candies = []
        for i in range(len(candiesLeft)):
            candies.append(max(candiesLeft[i], candiesRight[i]))
        
        return sum(candies)
        
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        boat = 0
        heavy = len(people)-1
        lightest = 0
        
        while(heavy>=lightest):
            boat+=1
            if people[heavy]+people[lightest]<=limit:
                lightest+=1
            heavy-=1
                    
        return(boat)
        
        
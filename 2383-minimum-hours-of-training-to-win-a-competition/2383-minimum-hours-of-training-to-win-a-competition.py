class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        runningEnergy = initialEnergy
        runningExperience = initialExperience
        extraExperience = 0
        m = len(energy)
        for i in range(m):
            runningEnergy-=energy[i]
            if experience[i]>=runningExperience+extraExperience:
                diff = experience[i] - (extraExperience+runningExperience)
                extraExperience+=diff+1
            runningExperience+=experience[i]
        
        if runningEnergy<=0:
            return abs(runningEnergy)+extraExperience+1
        return extraExperience
                            
        
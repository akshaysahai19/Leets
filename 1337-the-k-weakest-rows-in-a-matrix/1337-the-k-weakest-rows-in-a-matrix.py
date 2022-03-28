class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = []
        for i in range(len(mat)):
            count = 0
            for val in mat[i]:
                if val==1:
                    count+=1
            soldiers.append([i,count])
        
        soldiers.sort(key=lambda x:x[1])
        
        answer = []
        for i in range(k):
            answer.append(soldiers[i][0])
        return answer
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        output = []
        mem = {}
        
        def backtrack(index = 1, curr = []):
            
            if len(curr)==k:  
                if tuple(curr) not in mem:
                    mem[tuple(curr)] = 1
                    output.append(curr[:])

            for i in range(index, n+1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()


        output = []
        for i in range(1, n+1):
            backtrack(i, [])

        return output
        
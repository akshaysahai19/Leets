class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pairs = []
        for i in range(0, rowIndex+1):
            curr = []
            for j in range(0, i+1):
                if j==0 or j==i:
                    curr.append(1)
                else:
                    curr.append(pairs[-1][j-1]+pairs[-1][j])
            pairs.append(curr)
        return pairs[rowIndex]
                
            
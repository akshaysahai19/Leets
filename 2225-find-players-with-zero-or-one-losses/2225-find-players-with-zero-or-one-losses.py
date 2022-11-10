class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = OrderedDict()
        winners = OrderedDict()
        allPlayers = {}
        
        for winner, loser in matches:
            if winner in winners:
                winners[winner]+=1
            else:
                winners[winner]=1
            
            if loser in losses:
                losses[loser]-=1
            else:
                losses[loser]=-1
            
            if winner not in allPlayers:
                allPlayers[winner] = 1
                # allPlayers.append(winner)
            if loser not in allPlayers:
                allPlayers[loser] = 1
                # allPlayers.append(loser)
        
        answer_l = []
        answer_r = []
        for player in allPlayers.keys():
            if player not in losses:
                answer_l.append(player)
            if player in losses:
                if losses[player]==-1:
                    answer_r.append(player)
        
        answer_l.sort()
        answer_r.sort()
        return [answer_l, answer_r]
            
            
        
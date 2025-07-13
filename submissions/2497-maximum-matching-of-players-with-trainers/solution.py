class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        i = len(players) - 1
        ret = 0
        for t in trainers[::-1]:
            while i >= 0 and players[i] > t:
                i -= 1
            if i >= 0:
                i -= 1
                ret += 1
            else:
                break

        return ret
        

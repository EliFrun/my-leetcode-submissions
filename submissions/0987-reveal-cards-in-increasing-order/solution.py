class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ret = []
        for i in deck[::-1]:
            if ret:
                v = ret.pop()
                ret = [v] + ret
            ret = [i] + ret

        return ret
        

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if all(suits[0] == x for x in suits):
            return "Flush"
        if max(Counter(ranks).values()) >= 3:
            return "Three of a Kind"
        if max(Counter(ranks).values()) >= 2:
            return "Pair"
        return "High Card"
        

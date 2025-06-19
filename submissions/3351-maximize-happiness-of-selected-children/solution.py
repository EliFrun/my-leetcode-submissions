class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        return sum(
            [
                max(0, v - i) for i,v in 
                enumerate(
                    reversed(
                        sorted(happiness)[len(happiness) - k:]
                    )
                )
            ]
        )
        

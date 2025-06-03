class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        unlocked = set()
        locked = set()
        keys_found = set()
        visited = set()
        for box in initialBoxes:
            if status[box] == 1:
                unlocked.add(box)
            else:
                locked.add(box)
        
        ret = 0
        while unlocked:
            nxt = set()
            nxt_locked = set()
            while unlocked:
                box = unlocked.pop()
                ret += candies[box]
                keys_found.update(keys[box])
                for box2 in containedBoxes[box]:
                    if status[box2] == 1 or box2 in keys_found:
                        nxt.add(box2)
                    else:
                        nxt_locked.add(box2)

            for box in locked:
                if box in keys_found:
                    nxt.add(box)
                else:
                    nxt_locked.add(box)

            locked = nxt_locked
            unlocked = nxt

        return ret
                
            


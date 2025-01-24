class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)
        diff = len(a.keys()) - len(b.keys())
        if diff == 0:
            if len(word1) == len(word2):
                return True
            if len(word1) == 1:
                return word1 in word2
            if len(word2) == 1:
                return word2 in word1
            if len([x for x in a.values() if x > 1]) and len([x for x in b.values() if x > 1]):
                return True

            candidates_a = [k for k,v in a.items() if v == 1 and k in b]
            candidates_b = [k for k,v in a.items() if v == 1 and k in a]
            return len(candidates_a) > 0 or len(candidates_b) > 0

        if abs(diff) > 2:
            return False

        longer = a if len(a.keys()) > len(b.keys()) else b
        shorter = b if len(a.keys()) > len(b.keys()) else a
        if abs(diff) == 1:
            # longer needs to give shorter a letter 
            # that shorter does not have and longer has more than 1 of
            # shorter needs to give longer a letter that longer does have
            # and shorter has more than 1 of
            longer_candidates = [k for k,v in longer.items() if k not in shorter and v > 1]
            shorter_candidates = [k for k,v in shorter.items() if k in longer and v > 1]
            if len(longer_candidates) > 0 and len(shorter_candidates) > 0:
                return True

            # longer needs to give shorter a letter 
            # that shorter does not have and longer has exactly 1 of
            # shorter needs to give longer a letter that longer does not have
            # and shorter has more than 1 of
            longer_candidates = [k for k,v in longer.items() if k not in shorter and v == 1]
            shorter_candidates = [k for k,v in shorter.items() if k not in longer and v > 1]
            if len(longer_candidates) > 0 and len(shorter_candidates) > 0:
                return True

            # longer needs to give shorter a letter 
            # that shorter does not have and longer has exactly 1 of
            # shorter needs to give longer a letter that longer does have
            # and shorter has exactly 1 of
            longer_candidates = [k for k,v in longer.items() if k not in shorter and v == 1]
            shorter_candidates = [k for k,v in shorter.items() if k in longer and v == 1]
            if len(longer_candidates) > 0 and len(shorter_candidates) > 0:
                return True

            # longer needs to give shorter a letter 
            # that shorter does have and longer has exactly 1 of
            # shorter needs to give longer a letter that longer does have
            # and shorter has exactly more than 1 of
            longer_candidates = [k for k,v in longer.items() if k in shorter and v == 1]
            shorter_candidates = [k for k,v in shorter.items() if k in longer and v > 1]
            if len(longer_candidates) > 0 and len(shorter_candidates) > 0:
                if len(longer_candidates) == 1 and len(shorter_candidates) == 1:
                    return longer_candidates[0] != shorter_candidates[0]
                return True

            return False

            


        if abs(diff) == 2:
            # longer needs to give shorter a letter than short does not have
            # and longer has exactly 1 of
            longer_candidates = [k for k,v in longer.items() if k not in shorter and v == 1]
            shorter_candidates = [k for k,v in shorter.items() if v > 1 and k in longer]
            return len(longer_candidates) > 0 and len(shorter_candidates) > 0


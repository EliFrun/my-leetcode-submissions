class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def to_mapped(val):
            return int(
                ''.join(
                    [
                    str(
                        mapping[int(x)]
                    ) for x in list(str(val))
                    ]))

        return sorted(nums, key=lambda x: to_mapped(x))

        

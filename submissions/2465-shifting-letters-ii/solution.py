class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)
        nums = [0] * (len(s) + 1)
        for l, r, x in shifts:
            x = 1 if x == 1 else -1
            diff[l] += x
            diff[r + 1] -= x

        nums[0] = diff[0]
        for i in range(0, len(nums)):
            nums[i] = nums[i - 1] + diff[i]

        return ''.join(
            [
                chr(97 + (ord(c) - 97 + 26 + i) % 26) for i, c in zip(nums, list(s))
            ]
        )
        
        

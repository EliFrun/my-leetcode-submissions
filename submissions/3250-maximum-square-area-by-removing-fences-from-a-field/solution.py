class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        sh = set()
        hFences = [1] + hFences + [m]

        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                sh.add(abs(hFences[j] - hFences[i]))

        vFences_set = set([1] + vFences + [n])
        vFences = sorted([1] + vFences + [n])
        for diff in reversed(sorted(sh)):
            for v in vFences:
                if v + diff > vFences[-1]:
                    break
                if v + diff in vFences_set:
                    return (diff) ** 2 % 1_000_000_007

        return -1

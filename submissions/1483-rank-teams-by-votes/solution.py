class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        lis = []
        for _ in range(len(votes[0])):
            lis.append(defaultdict(int))
        for vote in votes:
            for i, c in enumerate(vote):
                lis[i][c] += 1
                
        nums = defaultdict(lambda: [0] * len(votes[0]))
        for c in votes[0]:
            for j, d in enumerate(lis):
                nums[c][j] = d[c]
        
        # a < b, a and b equal length
        def compare(a, b):
            a_c = a[1]
            b_c = b[1]
            a = a[0]
            b = b[0]
            for i in range(len(a)):
                if a[i] < b[i]:
                    return 1
                elif a[i] > b[i]:
                    return -1    
            return -1 if a_c < b_c else 1

        lis = []
        for c in votes[0]:
            lis.append((nums[c], c))
        
        lis.sort(key=cmp_to_key(compare))
        return "".join([x[1] for x in lis])
    

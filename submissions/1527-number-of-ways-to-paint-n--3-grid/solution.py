class Solution:
    def numOfWays(self, n: int) -> int:
        # states
        # 0  RYR
        # 1  RYG
        # 2  RGR
        # 3  RGY
        # 4  GYG
        # 5  GYR
        # 6  GRG
        # 7  GRY
        # 8  YRY
        # 9  YRG
        # 10 YGY
        # 11 YGR
        # 12 total states, need to count state transitions
        
        # can compute this
        states = [
            'RYR',
            'RYG',
            'RGR',
            'RGY',
            'GYG',
            'GYR',
            'GRG',
            'GRY',
            'YRY',
            'YRG',
            'YGY',
            'YGR'
        ]
        
        transition_list = defaultdict(list)
        for i, state in enumerate(states):
            for j, state2 in enumerate(states):
                if all(s1 != s2 for s1, s2 in zip(state, state2)):
                    transition_list[i].append(j)
                    
        curr = [1] * 12
        
        for _ in range(n - 1):
            nxt = [0] * 12
            for i in range(12):
                for j in transition_list[i]:
                    nxt[i] = (nxt[i] + curr[j]) % 1_000_000_007
                    
            curr = nxt
            
        return sum(curr) % 1_000_000_007
        

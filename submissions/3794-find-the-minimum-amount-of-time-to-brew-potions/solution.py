class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        prefix = [0]
        for m in skill:
            prefix.append(prefix[-1] + m)
        
        earliest_start = 0
        finish_time = [0] * len(skill)
        for j, m in enumerate(mana):
            finish_time[0] = earliest_start + m * skill[0]
            earliest_start = finish_time[0]
            for i in range(1, len(finish_time)):
                finish_time[i] = finish_time[i - 1] +  m * skill[i]
                if j < len(mana) - 1 and (v := finish_time[i] - mana[j + 1] * prefix[i]) > earliest_start:
                    earliest_start = v

        return finish_time[-1]
            
            


        

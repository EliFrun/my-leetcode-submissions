class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ret_list = []
        prev_val = 0
        current_val = 501
        max_val = 0
        for i in groupSizes:
            if i < current_val and i > prev_val:
                current_val = i
            if i > max_val:
                max_val = i

        while current_val <= max_val:
            temp_list = []
            for i in range(len(groupSizes)):
                if groupSizes[i] == current_val: 
                    if len(temp_list) < current_val:
                        temp_list.append(i)
                    else:
                        ret_list.append(temp_list)
                        temp_list = [i]
            
            
            ret_list.append(temp_list)                
            prev_val = current_val
            current_val = 501
            for i in groupSizes:
                if i < current_val and i > prev_val:
                    current_val = i
            
        return ret_list

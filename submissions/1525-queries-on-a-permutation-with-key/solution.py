class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        my_list = list(range(1, m + 1))
        ret = []
        for i in queries:
            ret.append(my_list.index(i))
            my_list.remove(i)
            my_list = [i] + my_list
            
        return ret

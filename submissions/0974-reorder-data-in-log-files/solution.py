class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums = [x for x in logs if x[-1].isnumeric()]
        lets = [x for x in logs if not x[-1].isnumeric()]
        
        def cmp(x, y):
            if x[len(x.split(" ")[0]):] > y[len(y.split(" ")[0]):]:
                return 1
            elif x[len(x.split(" ")[0]):] < y[:len(y.split(" ")[0])]:
                return -1
            
            return 1 if x[:len(x.split(" ")[0])] > y[:len(y.split(" ")[0]):] else -1
        
        lets.sort(key=cmp_to_key(lambda x,y: cmp(x,y)))
        
        return lets + nums

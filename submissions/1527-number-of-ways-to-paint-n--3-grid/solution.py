M = 1_000_000_007

def matmul(a, b):
    ret = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                ret[i][j] = (ret[i][j] + a[i][k] * b[k][j]) % M
    return ret

def matadd(a,b):
    ret = [[0] * len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            ret[i][j] = (a[i][j] + b[i][j]) % M
    return ret

l = [[0],[1],[2]]
for i in range(2):
    new_l = []
    for i in range(3):
        for lis in l:
            if lis[-1] != i:
                new_l.append(lis + [i])
    l = new_l

l.sort()
transition_matrix = [[0] * len(l) for _ in range(len(l))]
for i in range(len(l)):
    for j in range(len(l)):
        if all(l[i][k] != l[j][k] for k in range(3)):
            transition_matrix[i][j] = 1

class Solution:
    def numOfWays(self, n: int) -> int:
        t = deepcopy(transition_matrix)
        ret = [[0] * len(l) for _ in range(len(l))]
        for i in range(12):
            ret[i][i] = 1
        n -= 1
        while n:
            if n & 1:
                ret = matmul(ret, t)
            t = matmul(t, t)
            n >>= 1
        ret = matmul(ret, [[1] for _ in range(12)])
        return sum(sum(r) for r in ret) % M

        

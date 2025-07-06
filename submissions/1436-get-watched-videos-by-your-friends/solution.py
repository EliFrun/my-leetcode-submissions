class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        curr = set([id])
        visited = set()
        lvl = 0
        while curr and lvl < level:
            nxt = set()
            for f in curr:
                visited.add(f)
                nxt.update(friends[f])

            curr = nxt - visited
            lvl += 1

        d = defaultdict(int)
        for f in curr:
            for v in watchedVideos[f]:
                d[v] += 1

        return [k for k,v in sorted(d.items(), key=lambda x: (x[1], x[0]))]

        

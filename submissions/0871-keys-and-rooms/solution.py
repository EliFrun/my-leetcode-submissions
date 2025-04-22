class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        curr = set([0])
        while curr:
            nxt = set()
            for room in curr:
                if room in visited:
                    continue
                visited.add(room)
                nxt.update(rooms[room])

            curr = nxt - visited

        return all([x in visited for x in range(len(rooms))])

        

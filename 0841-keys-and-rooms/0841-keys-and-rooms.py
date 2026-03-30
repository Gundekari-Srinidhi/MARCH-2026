class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n =len(rooms)
        v = [0]*n
        q = []
        q.append(0)
        v[0] = 1
        while q:
            node = q.pop(0)
            for i in rooms[node]:
                if v[i] == 0:
                    v[i] = 1
                    q.append(i)
        for i in v:
            if i == 0:
                return False
        return True
            
        
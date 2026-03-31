class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = []
        for _ in range(n):
            adj.append([])
        
        for i,j in connections:
            adj[i].append((j,1))
            adj[j].append((i,0))
        v = [0]*n
        count = 0
        q = []
        q.append(0)
        v[0] = 1
      
        while q:
            node = q.pop(0)
            for j,val in adj[node]:
                if v[j] == 0:
                    count+=val
                    v[j] = 1
                    q.append(j)
        return count

        
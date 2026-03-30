class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = []
        for _ in range(n):
            adj.append([])
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j] == 1:
                    adj[i].append(j)
        
        v = [0]*n
        
        count = 0
        for i in range(n):
            if v[i] == 0:
                q = []
                q.append(i)
                v[i] = 1
                count+=1
                while q:
                    node = q.pop(0)
                    for j in adj[node]:
                        if v[j] == 0:
                            v[j] = 1
                            q.append(j)
        return count



        
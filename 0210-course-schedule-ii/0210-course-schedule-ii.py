class Solution:
    def findOrder(self, num: int, p: List[List[int]]) -> List[int]:
        adj = []
        indegree = [0]*num
        for _  in range(num):
            adj.append([])
        
        for n,m in p:
            adj[m].append(n)
        
        q = []
        ans = []
        for i in  range(num):
            for j in adj[i]:
                indegree[j]+=1
        
        for i in range(num):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node=q.pop(0)
            ans.append(node)

            for val in adj[node]:
                indegree[val]-=1
                if indegree[val] == 0:
                    q.append(val)
        if len(ans) == num:
            return ans
        return []
        
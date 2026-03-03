class RecentCounter:

    def __init__(self):
        self.arr=[]
        

    def ping(self, t: int) -> int:
        self.arr.append(t)
        count=0
        for val in self.arr:
            if t-3000<=val<=t:
                count+=1
        return count
        

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
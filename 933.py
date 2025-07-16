from collections import deque

class RecentCounter:
    def __init__(self):
        self.recent = deque()

    def ping(self, t: int) -> int:
        self.recent.append(t)
        x = self.recent.popleft()
        while(x < t - 3000):
            if(self.recent):
                x = self.recent.popleft()
        self.recent.appendleft(x)
        return len(self.recent)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
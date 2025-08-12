from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue, d_queue = deque(), deque()

        for index, senator in enumerate(senate):
            if(senator == 'R'):
                r_queue.append(index)
            else:
                d_queue.append(index)

        while(d_queue and r_queue):
            if(d_queue[0] < r_queue[0]):
                x = d_queue.popleft()
                r_queue.popleft()
                d_queue.append(x + len(senate))
            else:
                d_queue.popleft()
                x = r_queue.popleft()
                r_queue.append(x + len(senate))

        return "Radiant" if r_queue else "Dire"
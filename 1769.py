class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left = [0]*len(boxes)
        right = [0]*len(boxes)

        balls = 0
        for i in range(1, len(boxes)):
            if boxes[i - 1] == '1':
                balls += 1
            left[i] = left[i - 1] + balls
        balls = 0
        for i in range(len(boxes) - 2, -1, -1):
            if boxes[i + 1] == '1':
                balls += 1
            right[i] = right[i + 1] + balls
        return [l + r for l, r in zip(left, right)]
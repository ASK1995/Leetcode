from collections import defaultdict

class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        count = defaultdict(lambda:set())
        max_count = 0
        for student, bench in students:
            count[bench].add(student)
            max_count = max(max_count, len(count[bench]))
        return max_count
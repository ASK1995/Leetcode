from collections import defaultdict

class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        benches = defaultdict(lambda:set())
        max_count = 0
        
        for student, bench in students:
            benches[bench].add(student)
            max_count = max(max_count, len(benches[bench]))

        return max_count
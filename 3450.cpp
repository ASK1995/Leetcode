class Solution {
public:
    int maxStudentsOnBench(vector<vector<int>>& students) {
        unordered_map<int, unordered_set<int>> student;
        int res = 0, max_bench = 0;

        for(int i = 0; i < students.size(); i++) {
            student[students[i][1]].insert(students[i][0]);
        }
        for(auto it = student.begin(); it != student.end(); it++) {
            if(it->second.size() > max_bench) {
                max_bench = it->second.size();
                res = it->first;
            }
        }
        return max_bench;
    }
};
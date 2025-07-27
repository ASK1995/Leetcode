class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        unordered_map<char, int> check, count;
        int res = 0;
        bool add;

        for(int i = 0; i < allowed.size(); i++) {
            check[allowed[i]]++;
        }

        for(int i = 0; i < words.size(); i++) {
            for(int j = 0; j < words[i].size(); j++) {
                count[words[i][j]]++;
            }
            add = true;
            for(auto it = count.begin(); it != count.end(); it++) {
                if(check[it->first] == 0) {
                    add = false;
                    break;
                }
            }
            if(add) {
                res += 1;
            }
            count.clear();
        }
        return res;
    }
};
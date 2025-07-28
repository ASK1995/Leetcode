class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> num;

        for(int i = 0; i < arr.size(); i++) {
            if(arr[i] % 2 == 0) {
                if(num.find(arr[i]/2) != num.end()) {
                    return true;
                }
            }
            if(num.find(arr[i] * 2) != num.end()) {
                return true;
            }
            num.insert(arr[i]);
        }
        return false;
    }
};
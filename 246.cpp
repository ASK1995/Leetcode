class Solution {
public:
    bool isStrobogrammatic(string num) {
        int l = 0, r = num.size() - 1;
        int left, right;

        while(l <= r){
            left = num[l];
            right = num[r];
            if(left == '6') {
                left = '9';
            } else if(left == '9') {
                left = '6';
            } else if(left == '0' || left == '1' || left == '8'){
                left = left;
            } else {
                return false;
            }

            if(left != right) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};
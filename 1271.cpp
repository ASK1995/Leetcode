class Solution {
public:
    string toHexspeak(string num) {
        string res = "";
        unordered_map<int, char> mapping;
        mapping[0] = 'O';
        mapping[1] = 'I';
        mapping[10] = 'A';
        mapping[11] = 'B';
        mapping[12] = 'C';
        mapping[13] = 'D';
        mapping[14] = 'E';
        mapping[15] = 'F';
        long long int number = stoll(num);
        while(number != 0){
            if (mapping.find(number % 16) != mapping.end()) {
                res += mapping[number % 16];
            } else {
                return "ERROR";
            }
            number /= 16;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
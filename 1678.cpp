class Solution {
public:
    string interpret(string command) {
        string res = "";
        for(int i = 0; i < command.size(); i++) {
            if(command[i] == '(') {
                if(command[i + 1] == ')') {
                    res += 'o';
                    i++;
                }
                else {
                    res += "al";
                    i += 3;
                }
            } else {
                res += 'G';
            }
        }
        return res;
    }
};
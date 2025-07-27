class Solution {
public:
    bool isValid(string s) {
        stack<char> letters;
        char letter;
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[') {
                letters.push(s[i]);
            } else {
                if(letters.size() == 0) {
                    return false;
                } else {
                    letter = letters.top();
                    if((letter == '{' && s[i] == '}') ||
                        (letter == '[' && s[i] == ']') ||
                        (letter == '(' && s[i] == ')'))
                    {
                        letters.pop();
                    } else {
                        return false;
                    }
                }
            }
        }
        if(letters.size() == 0) {
            return true;
        }
        return false;
    }
};
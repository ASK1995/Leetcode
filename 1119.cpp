class Solution {
public:
    string removeVowels(string s) {
        string res = "";
        unordered_set<char> vowels;

        vowels.insert('a');
        vowels.insert('e');
        vowels.insert('i');
        vowels.insert('o');
        vowels.insert('u');
        
        for(int i = 0; i < s.size(); i++) {
            if(vowels.find(s[i]) == vowels.end()) {
                res += s[i];
            }
        }
        return res;
    }
};
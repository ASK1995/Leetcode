class Solution {
public:
    bool checkIfPangram(string sentence) {
        unordered_set<char> letters;

        for(int i = 0; i < sentence.size(); i++) {
            letters.insert(sentence[i]);
        }
        for(int i = 97; i <= 122; i++) {
            if(letters.find(i) == letters.end()) {
                return false;
            }
        }
        return true;
    }
};
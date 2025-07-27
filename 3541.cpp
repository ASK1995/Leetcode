class Solution {
public:
    int maxFreqSum(string s) {
        unordered_set<char> vowels;
        unordered_map<char, int> count;
        int freq_v = 0, freq_c = 0;
        vowels.insert('a');
        vowels.insert('e');
        vowels.insert('i');
        vowels.insert('o');
        vowels.insert('u');

        for(int i = 0; i < s.size(); i++) {
            count[s[i]]++;
        }

        for(auto it = count.begin(); it != count.end(); it++) {
            if(vowels.find(it->first) != vowels.end()) {
                freq_v = fmax(freq_v, it->second);
            } else {
                freq_c = fmax(freq_c, it->second);
            }
        }
        return freq_v + freq_c;
    }
};
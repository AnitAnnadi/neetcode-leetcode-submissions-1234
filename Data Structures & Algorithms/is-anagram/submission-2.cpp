class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        unordered_map<char, int> countsS;
        unordered_map<char, int> countsT;

        for (int i = 0; i < s.size(); i++) {
            countsS[s[i]]++;
            countsT[t[i]]++;
        }

        return countsS == countsT;
    }
};
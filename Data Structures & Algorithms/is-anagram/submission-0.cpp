class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        unordered_map<char, int> counts;

        for (char c : s) {
            if (!counts.count(c)) {
                counts[c] = 0;
            }

            counts[c]++;
        } 

        for (char c : t) {
            if (!counts.count(c) || counts[c] == 0) return false;
            counts[c]--;
        }

        return true;
    }
};
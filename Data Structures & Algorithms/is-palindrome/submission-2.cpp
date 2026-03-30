class Solution {
public:
    bool isPalindrome(string s) {
        string newS = "";
        for (char c : s) {
            if (!isalnum(c)) continue;

            newS += tolower(c);
        }

        int R = newS.size() - 1;
        int L = 0;

        while (L < newS.size()) {
            if (newS[L] != newS[R]) return false;

            L++;
            R--;
        }

        return true;
    }
};

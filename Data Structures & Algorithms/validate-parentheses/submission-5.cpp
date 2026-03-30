class Solution {
public:
    bool isValid(string s) {

        unordered_map<char, char> parentheses= {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'},
        };

        stack<int> openingParentheses;

        for (int i = 0; i < s.size(); i++) {
            if (parentheses.count(s[i])) {
                openingParentheses.push(s[i]);
            } else {
                if (!openingParentheses.empty() && parentheses[openingParentheses.top()] == s[i]) {
                    openingParentheses.pop();
                } else {
                    return false;
                }
            }
        }

        return openingParentheses.empty();
    }
};

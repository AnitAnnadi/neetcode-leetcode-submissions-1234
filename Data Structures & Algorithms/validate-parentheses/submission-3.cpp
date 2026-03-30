class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> matchingParentheses = {
            {')', '('},
            {'}', '{'},
            {']', '['},
        };

        stack<char> stack;

        for (char c : s) {
            if(matchingParentheses.count(c)) {
                if (!stack.empty() && matchingParentheses[c] == stack.top()) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.empty();
    }
};

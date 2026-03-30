class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> matchingParentheses = {
            {')', '('},
            {'}', '{'},
            {']', '['},
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };
        vector<char> stack;

        for (int i = 0; i < s.size(); i++) {
            stack.push_back(s[i]);
        }

        int stackPointer = stack.size() - 1;
        for (int i = 0; i < s.size() / 2; i++) {
            if(matchingParentheses[stack[stackPointer]] != s[i]) {
                return false;
            }

            stack.pop_back();
            stackPointer--;
        }

        return true;
    }
};

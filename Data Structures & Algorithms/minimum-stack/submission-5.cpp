class MinStack {
public:
    MinStack() {}
    
    void push(int val) {
        stack.push_back(val);

        if (minimums.empty()) {
            minimums.push_back(val);
        } else {
            if (val < minimums[minimums.size() - 1]) {
                minimums.push_back(val);
            } else {
                minimums.push_back(minimums[minimums.size() - 1]);
            }
        }
    }
    
    void pop() {
        stack.pop_back();
        minimums.pop_back();
    }
    
    int top() {
        return stack[stack.size() - 1];
    }
    
    int getMin() {
        return minimums[minimums.size() - 1];
    }

    private: 
        vector<int> stack;
        vector<int> minimums;
};

class MinStack {
public:
    MinStack() {
        hasMin = false;
    }
    
    void push(int val) {
        stack.push_back(val);

        if (!hasMin) {
            min = val;
            hasMin = true;
        } else {
            if (val < min) {
                min = val;
            }
        }
    }
    
    void pop() {
        stack.pop_back();

        min = stack[0];
        for (int i = 1; i < stack.size(); i++) {
            if (stack[i] < min) {
                min = stack[i];
            }
        }
    }
    
    int top() {
        return stack[stack.size() - 1];
    }
    
    int getMin() {
        return min;
    }

    private:
        vector<int> stack;
        bool hasMin;
        int min;
};

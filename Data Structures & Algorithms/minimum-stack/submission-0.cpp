class MinStack {
public:
    MinStack() {
        min = NULL;
    }
    
    void push(int val) {
        stack.push_back(val);

        if (!min) {
            min = val;
            cout << "worked";
        } else {
            if (val < min) {
                min = val;
            }
        }
    }
    
    void pop() {
        stack.pop_back();

        min = stack[0];
        for (int i = 0; i < stack.size(); i++) {
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
        int min;
};

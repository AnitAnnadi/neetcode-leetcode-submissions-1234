class MyStack {
private:
    queue<int> q1;
    queue<int> q2;
public:
    MyStack() {
        
    }
    
    void push(int x) {
        if (q1.empty()) {
            q1.push(x);

            for (int i = 0; i < q2.size(); i++) {
                q1.push(q2.front());
                q2.pop();
            }
        } else {
            q2.push(x);

            for (int i = 0; i < q1.size(); i++) {
                q2.push(q1.front());
                q1.pop();
            }
        }
    }
    
    int pop() {
        int val;
        if (q1.empty()) {
            val = q2.front();
            q2.pop();
        } else {
            val = q1.front();
            q1.pop();
        }

        return val;
    }
    
    int top() {
        int val;
        if (q1.empty()) {
            val = q2.front();
        } else {
            val = q1.front();
        }

        return val;
    }
    
    bool empty() {
        return q1.empty() && q2.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
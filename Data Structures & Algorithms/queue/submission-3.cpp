struct Node {
    int val;
    Node* prev;
    Node* next;

    Node(int val) {
        this->val = val;
        prev = nullptr;
        next = nullptr;
    }
};

class Deque {
private:
    Node* head;
    Node* tail;
public:
    Deque() {
        head = new Node(-1);
        tail = head;
    }

    bool isEmpty() {
        if (head->next == nullptr) {
            return true;
        } 

        cout << head->next->val << endl;

        return false;
    }

    void append(int value) {
        Node* newNode = new Node(value);
        tail->next = newNode;
        newNode->prev = tail;
        tail = tail->next;
    }

    void appendleft(int value) {
        Node* newNode = new Node(value);

        if (head->next != nullptr) {
            head->next->prev = newNode;
        } else {
            tail = newNode;
        }

        newNode->next = head->next;
        newNode->prev = head;
        head->next = newNode;
    }

    int pop() {
        if (head == tail) {
            return -1;
        }

        Node* nodeToRemove = tail;
        int val = nodeToRemove->val;
        tail->prev->next = nullptr;
        tail = tail->prev;
        delete nodeToRemove;
        return val;
    }

    int popleft() {
        if (head == tail) {
            return -1;
        }

        Node* nodeToRemove = head->next;
        int val = nodeToRemove->val;
        head->next = nodeToRemove->next;

        if (nodeToRemove->next != nullptr) {
            nodeToRemove->next->prev = head;
        } else {
            tail = head;
        }

        delete nodeToRemove;
        return val;
    }
};

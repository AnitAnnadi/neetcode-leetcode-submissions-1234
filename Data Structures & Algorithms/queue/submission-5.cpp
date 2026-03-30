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
    Node* dummyHead;
    Node* dummyTail;
public:
    Deque() {
        dummyHead = new Node(-1);
        dummyTail = new Node(-1);
        dummyHead->next = dummyTail;
        dummyTail->prev = dummyHead;
    }

    bool isEmpty() {
        if (dummyHead->next == dummyTail) {
            return true;
        }

        return false;
    }

    void append(int value) {
        Node* newNode = new Node(value);

        newNode->prev = dummyTail->prev;
        newNode->next = dummyTail;
        dummyTail->prev->next = newNode;
        dummyTail->prev = newNode;
    }

    void appendleft(int value) {
        Node* newNode = new Node(value);

        newNode->prev = dummyHead;
        newNode->next = dummyHead->next;
        dummyHead->next->prev = newNode;
        dummyHead->next = newNode;
    }

    int pop() {
        if(this->isEmpty()) {
            return -1;
        }

        Node* nodeToRemove = dummyTail->prev;
        int val = nodeToRemove->val;

        nodeToRemove->prev->next = dummyTail;
        dummyTail->prev = nodeToRemove->prev;
        
        delete nodeToRemove;
        return val;
    }

    int popleft() {
        if (this->isEmpty()) {
            return -1;
        }

        Node* nodeToRemove = dummyHead->next;
        int val = nodeToRemove->val;

        nodeToRemove->next->prev = dummyHead;
        dummyHead->next = nodeToRemove->next;

        delete nodeToRemove;
        return val;
    }
};

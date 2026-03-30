struct Node {
    int data;
    Node* next = nullptr;

    Node(int data) {
        this->data = data;
    }
};

class LinkedList {
private:
    Node* head;
    Node* tail;
    int length;
public:
    LinkedList() {
        head = nullptr;
        tail = nullptr;
        length = 0;
    }

    int get(int index) {
        if (index >= length) {
            return -1;
        }

        Node* currNode = head;
        for(int i = 0; i < index; i++) {
            currNode = currNode->next;
        }

        return currNode->data;
    }

    void insertHead(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = tail = newNode;
            length++;
            return;
        }

        newNode->next = head;
        head = newNode;
        length++;
    }
    
    void insertTail(int val) {
        Node* newNode = new Node(val);
        if (tail == nullptr) {
            tail = head = newNode;
            length++;
            return;
        }

        tail->next = newNode;
        tail = newNode;
        length++;
    }

    bool remove(int index) {
        if (index >= length) {
            return false;
        }

        if (index == 0) {
            Node* tmpPtr = head;
            head = tmpPtr->next;
            delete tmpPtr;

            if (length == 1) {
                tail = nullptr;
            }

            length--;
            return true;
        }

        Node* prevNode;
        Node* currNode = head;
        for(int i = 0; i < index; i++) {
            prevNode = currNode;
            currNode = currNode->next;
        }

        if (index == length - 1) {
            prevNode->next = nullptr;
            tail = prevNode;
        } else {
            prevNode->next = prevNode->next->next;
        }

        delete currNode;
        length--;
        return true;
    }

    vector<int> getValues() {
        vector<int> values;

        Node* currNode = head;
        while(currNode != nullptr) {
            values.push_back(currNode->data);
            currNode = currNode->next;
        }

        return values;
    }
};

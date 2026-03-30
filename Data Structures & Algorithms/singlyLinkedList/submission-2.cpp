struct Node {
    int data;
    Node* next;

    Node(int data) {
        this->data = data;
        next = nullptr;
    }
};

class LinkedList {
private:
    Node* head;
    Node* tail;
public:
    LinkedList() {
        head = new Node(-1);
        tail = head;
    }

    int get(int index) {
        Node* currNode = head->next;
        
        int i = 0;
        while(currNode != nullptr) {
            if (index == i) {
                return currNode->data;
            }

            currNode = currNode->next;
            i++;
        }
        return -1;
    }

    void insertHead(int val) {
        Node* newNode = new Node(val);
        newNode->next = head->next;
        head->next = newNode;

        if (newNode->next == nullptr) {
            tail = newNode;
        }
    }
    
    void insertTail(int val) {
        Node* newNode = new Node(val);
        tail->next = newNode;
        tail = newNode;
    }

    bool remove(int index) {
        Node* prevNode = head;

        int i = 0;
        while (prevNode != nullptr && i < index) {
            prevNode = prevNode->next;
            i++;
        }

        if (prevNode != nullptr && prevNode->next != nullptr) {
            if (prevNode->next == tail) {
                tail = prevNode;
            }

            Node* tmpNode = prevNode->next;
            prevNode->next = prevNode->next->next;
            delete tmpNode;
            return true;
        }

        return false;
    }

    vector<int> getValues() {
        vector<int> nums;

        Node* currNode = head->next;
        while(currNode != nullptr) {
            nums.push_back(currNode->data);
            currNode = currNode->next;
        }

        return nums;
    }
};

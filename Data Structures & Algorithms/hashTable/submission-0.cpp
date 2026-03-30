struct Node {
    int key;
    int val;
    Node* next;

    Node(int key, int val) {
        this->key = key;
        this->val = val;
        next = nullptr;
    }
};

class HashTable {
    int capacity;
    int size;
    vector<Node*> hp;

    int hash(int key) {
        return key % capacity;
    }
public:
    HashTable(int capacity) {
        this->capacity = capacity;
        size = 0;

        for (int i = 0; i < capacity; i++) {
            hp.push_back(nullptr);
        }
    }

    void insert(int key, int value) {
        int index = hash(key);
        Node* tmpPtr = hp[index];

        if (tmpPtr == nullptr) {
            hp[index] = new Node(key, value);
            size += 1;
            if (size >= capacity / 2) resize();
            return;
        }

        Node* prevPtr = nullptr;
        while (tmpPtr != nullptr) {
            if (tmpPtr->key == key) {
                tmpPtr->val = value;
                return;
            }

            prevPtr = tmpPtr;
            tmpPtr = tmpPtr->next;
        }

        prevPtr->next = new Node(key, value);
        size += 1;
        if (size >= capacity / 2) resize();
    }

    int get(int key) {
        int index = hash(key);
        Node* tmpPtr = hp[index];

        while (tmpPtr != nullptr) {
            if (tmpPtr->key == key) return tmpPtr->val;
            tmpPtr = tmpPtr->next;
        }

        return -1;
    }

    bool remove(int key) {
        int index = hash(key);
        Node* tmpPtr = hp[index];

        if (tmpPtr == nullptr) return false;

        if (tmpPtr->key == key) {
            hp[index] = tmpPtr->next;
            delete tmpPtr;
            size -= 1;
            return true;
        }

        Node* prevPtr = nullptr;
        while (tmpPtr != nullptr) {
            if (tmpPtr->key == key) {
                prevPtr->next = tmpPtr->next;
                delete tmpPtr;
                size -= 1;
                return true;
            }

            prevPtr = tmpPtr;
            tmpPtr = tmpPtr->next;
        }

        return false;
    }

    int getSize() const {
        return size;
    }

    int getCapacity() const {
        return capacity;
    }

    void resize() {
        capacity = capacity * 2;
        vector<Node*> oldHp = hp;
        hp = vector<Node*>(capacity, nullptr);
        size = 0;


        for(int i = 0; i < capacity / 2; i++) {
            Node* tmpPtr = oldHp[i];
            while (tmpPtr != nullptr) {
                insert(tmpPtr->key, tmpPtr->val);
                tmpPtr = tmpPtr->next;
            }
        }
    }
};

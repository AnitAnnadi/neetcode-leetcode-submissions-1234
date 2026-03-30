struct Node {
    int key;
    int val;
    Node* prev;
    Node* next;

    Node (int key, int val) {
        this->key = key;
        this->val = val;
        prev = next = nullptr;
    }
};

class LRUCache {
private:
    int capacity;
    unordered_map<int, Node*> m;
    Node* left;
    Node* right;

    void insert(Node* node) {
        node->prev = right->prev;
        node->next = right;
        right->prev->next = node;
        right->prev = node;
    }

    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
public:
    LRUCache(int capacity) {
        this->capacity = capacity;

        left = new Node(0, 0);
        right = new Node(0, 0);

        left->next = right;
        right->prev = left;
    }
    
    int get(int key) {
        if (m.count(key)) {
            Node* node = m.find(key)->second;

            remove(node);
            insert(node);

            return node->val;
        }

        return -1;
    }
    
    void put(int key, int value) {
        if (m.count(key)) {
            Node* node = m.find(key)->second;
            remove(node);
            delete node;
        }

        Node* newNode = new Node(key, value);
        insert(newNode);
        m[key] = newNode;

        if (m.size() > capacity) {
            Node* nodeToRemove = left->next;
            remove(nodeToRemove);
            m.erase(nodeToRemove->key);
            delete nodeToRemove;
        }
    }
};

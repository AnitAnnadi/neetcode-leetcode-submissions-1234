class LRUCache {
private:
    unordered_map<int, int> m;
    vector<int> keyUseOrder;
    int capacity;
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if (m.count(key)) {
            keyUseOrder.push_back(key);
            cout << keyUseOrder[0];
            return m.find(key)->second;
        }

        return -1;
    }
    
    void put(int key, int value) {
        if (!m.count(key) && m.size() >= capacity && !keyUseOrder.empty()) {
            int lastKey = keyUseOrder[keyUseOrder.size() - 1];
            vector<int> tmp = {};

            m.erase(lastKey);

            for(int i = 0; i < keyUseOrder.size(); i++) {
                if (keyUseOrder[i] != lastKey) {
                    tmp.push_back(keyUseOrder[i]);
                }
            }
            keyUseOrder = tmp;
        }

        m[key] = value;
    }
};

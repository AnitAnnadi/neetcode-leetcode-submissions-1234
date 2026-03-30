class LRUCache {
private:
    unordered_map<int, int> m;
    int capacity;
    set<int> s;
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if (m.count(key)) {

            if (s.count(key)) {
                s.erase(key);
                s.insert(key);
            }

            return m.find(key)->second;
        }

        return -1;
    }
    
    void put(int key, int value) {
        if (!m.count(key) && m.size() >= capacity) {
            int lastKey = *s.begin();
            m.erase(lastKey);
            s.erase(lastKey);
        }

        s.insert(key);
        m[key] = value;
    }
};

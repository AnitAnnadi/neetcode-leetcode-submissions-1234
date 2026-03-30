class MinHeap {
    vector<int> heap_;
public:
    MinHeap() {
        heap_.push_back(0);
    }

    void push(int val) {
        heap_.push_back(val);

        int curr = heap_.size() - 1;
        while (curr > 1) {
            int parent = curr / 2;
            if (heap_[curr] < heap_[parent]) {
                swap(heap_[curr], heap_[parent]);
                curr = parent;
            } else {
                break;
            }
        }
    }

    int pop() {
        if (heap_.size() == 1) {
            return -1;
        }

        int minVal = heap_[1];

        if (heap_.size() == 2) {
            heap_.pop_back();
            return minVal;
        }

        heap_[1] = heap_[heap_.size() - 1];
        heap_.pop_back();
        heapifyDown(1);

        return minVal;
    }

    int top() {
        if (heap_.size() == 1) {
            return -1;
        }

        return heap_[1];
    }

    void heapify(const vector<int>& arr) {
        heap_ = {0};
        for (int i = 0; i < arr.size(); i++) {
            heap_.push_back(arr[i]);
        }

        int curr = (heap_.size() - 1) / 2;
        while (curr > 0) {
            heapifyDown(curr);
            curr -= 1;
        }
    }
    private:
    void heapifyDown(int i) {
        while (2 * i < heap_.size()) {
            if (2 * i + 1 < heap_.size() && heap_[2*i + 1] < heap_[2*i] && heap_[2*i + 1] < heap_[i]) {
                swap(heap_[i], heap_[2*i + 1]);
                i = 2*i + 1;
            } else if (heap_[2*i] < heap_[i]) {
                swap(heap_[i], heap_[2*i]);
                i = 2*i;
            } else {
                break;
            }
        }
    }
};

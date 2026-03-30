class DynamicArray {
private:
    int* arr;
    int capacity;
    int size;

public:

    DynamicArray(int capacity) {
        arr = new int[capacity];
        this->capacity = capacity;
        size = 0;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) {
            resize();
        }

        arr[size++] = n; 
    }

    int popback() {
        return arr[--size];
    }

    void resize() {
        capacity *= 2;
        int* tmpArr = new int[capacity];

        for (int i = 0; i < size; i++) {
            tmpArr[i] = arr[i];
        }

        delete arr;
        arr = tmpArr;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};

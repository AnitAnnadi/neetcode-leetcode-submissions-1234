class DynamicArray {
private:
    int capacity;
    int size;
    int* arr;

public:

    DynamicArray(int capacity) {
        this->capacity = capacity;
        size = 0;
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (capacity == size) {
            resize();
        }

        arr[size] = n;
        size++;
    }

    int popback() {
        int pop = arr[size - 1];
        arr[size - 1] = 0;
        size--;
        return pop;
    }

    void resize() {
        int* arrTemp = arr;
        capacity *= 2;

        arr = new int[capacity];
        for (int i = 0; i < size; i++) {
            arr[i] = arrTemp[i];
        }

        delete[] arrTemp;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};

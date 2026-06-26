public class DynamicArray {
    private int capacity;
    private int size;
    private int[] list;
    
    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.list = new int[capacity];
    }

    public int Get(int i) {
        return list[i];
    }

    public void Set(int i, int n) {
        list[i] = n;
    }

    public void PushBack(int n) {
        if (size >= capacity)
            this.Resize();

        size++;
        list[size - 1] = n;
    }

    public int PopBack() {
        var value = list[size-1];
        size--;
        return value;
    }

    private void Resize() {
        capacity = capacity * 2;
        var newList = new int[capacity];

        Array.Copy(list, newList, size);

        list = newList;
    }

    public int GetSize() {
        return size;
    }

    public int GetCapacity() {
        return capacity;
    }
}

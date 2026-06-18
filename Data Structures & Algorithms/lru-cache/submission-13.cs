public class Node {
    public int key;
    public int value;
    public Node next;
    public Node previous;

    public Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.next = null;
        this.previous = null;
    }
}
public class LRUCache {
    private Node head;
    private Node tail;
    private int capacity;
    private Dictionary<int, Node> nodes;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.nodes = new Dictionary<int, Node>();
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        head.next = tail;
        tail.previous = head;
    }

    private void InsertList(Node node) {
        Node previous = tail.previous;

        previous.next = node;
        tail.previous = node;

        node.next = tail;
        node.previous = previous;
    }

    private void DeleteList(Node node) {
        Node previous = node.previous;
        Node next = node.next;
        previous.next = next;
        next.previous = previous;
    }
    
    public int Get(int key) {
        if (!nodes.ContainsKey(key)) {
            return -1;
        }

        Node curr = nodes[key];
        DeleteList(curr);
        InsertList(curr);

        return nodes[key].value;
    }
    
    public void Put(int key, int value) {
        if (nodes.ContainsKey(key)) {
            Node curr = nodes[key];
            curr.value = value;

            DeleteList(curr);
            InsertList(curr);
            return;
        }

        if (nodes.Count >= capacity) {
            Node lru = head.next;
            nodes.Remove(lru.key);
            DeleteList(lru);
        }

        Node newNode = new Node(key, value);
        nodes.Add(key, newNode);
        InsertList(newNode);
    }
}
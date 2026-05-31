public class MinStack {

    private Stack<(int, int)> stack;

    public MinStack() {
        this.stack = new Stack<(int, int)>();
    }
    
    public void Push(int val) {
        if (this.stack.Count == 0) {
            var newElement = (val, val);
            stack.Push(newElement);
        } else {
            var currStackMin = this.GetMin();
            var minElement = Math.Min(val, currStackMin);

            var newElement = (val, minElement);
            stack.Push(newElement);
        }
    }
    
    public void Pop() {
        stack.Pop();
    }
    
    public int Top() {
        (var top, var min) = stack.Peek();
        return top;
    }
    
    public int GetMin() {
        (var top, var min) = stack.Peek();
        return min;
    }
}

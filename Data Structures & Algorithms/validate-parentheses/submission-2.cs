public class Solution {
    public bool IsValid(string s) {
        var stack = new Stack<char>();
        var brackets = new Dictionary<char, char>() {
            { '{', '}'},
            { '[', ']'},
            { '(', ')'}
        };

        foreach (var c in s) {
            switch (c) {
                case '{':
                case '[':
                case '(':
                    stack.Push(brackets[c]);
                    break;
                case '}':
                case ']':
                case ')':
                    if (stack.Count() == 0) {
                        return false;
                    }
                    
                    if (stack.Pop() != c) {
                        return false;
                    }
                break;
            }
        }

        if (stack.Count() > 0) {
            return false;
        }

        return true;


    }
}

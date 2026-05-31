public class Solution {
    public bool IsPalindrome(string s) {
        var sb = new StringBuilder();

        foreach(var c in s) {
            if (Char.IsLetterOrDigit(c)) {
                sb.Append(Char.ToLower(c));
            }
        }

        var sanitisedString = sb.ToString();

        int i = 0;
        int j = sanitisedString.Length - 1;

        while (i < j) {
            if (sanitisedString[i] != sanitisedString[j]) {
                return false;
            }

            i++;
            j--;
        }

        return true;
    }
}

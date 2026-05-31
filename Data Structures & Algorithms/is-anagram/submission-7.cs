public class Solution {
    public bool IsAnagram(string s, string t) {
        var lettersS = new Dictionary<char, int>();
        var lettersT = new Dictionary<char, int>();

        foreach (var c in s) {
            if (lettersS.ContainsKey(c)) {
                lettersS[c]++;
            } else {
                lettersS[c] = 1;
            }
        }

        foreach (var c in t) {
            if (lettersT.ContainsKey(c)) {
                lettersT[c]++;
            } else {
                lettersT[c] = 1;
            }
        }

        if (lettersS.Count != lettersT.Count) {
            return false;
        }

        foreach (var kvp in lettersS) {
            if (!lettersT.ContainsKey(kvp.Key) || lettersT[kvp.Key] != kvp.Value) {
                return false;
            }
        }

        return true;
    }
}

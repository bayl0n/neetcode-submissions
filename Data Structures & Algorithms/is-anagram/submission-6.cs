public class Solution {
    public bool IsAnagram(string s, string t) {
        var letterMapS = new Dictionary<char, int>();
        var letterMapT = new Dictionary<char, int>();

        foreach (var c in s) {
            var lowerC = char.ToLower(c);
            if (letterMapS.ContainsKey(lowerC)) {
                letterMapS[lowerC]++;
            } else if (Char.IsLetterOrDigit(lowerC)) {
                letterMapS[lowerC] = 1;
            }
        }

        foreach (var c in t) {
            var lowerC = char.ToLower(c);
            if (letterMapT.ContainsKey(lowerC)) {
                letterMapT[lowerC]++;
            } else if (Char.IsLetterOrDigit(lowerC)) {
                letterMapT[lowerC] = 1;
            }
        }

        if (letterMapS.Count() != letterMapT.Count()) {
            return false;
        }

        foreach (var kvp in letterMapS) {
            if (!letterMapT.ContainsKey(kvp.Key) || kvp.Value != letterMapT[kvp.Key]) {
                return false;
            }
        }

        return true;
    }
}

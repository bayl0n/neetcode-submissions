public class Solution {
    public bool IsAnagram(string s, string t) {
        var sDict = new Dictionary<char, int>();
        var tDict = new Dictionary<char, int>();

        foreach (var c in s) {
            if (sDict.ContainsKey(c)) {
                sDict[c]++;
            } else {
                sDict[c] = 1;
            }
        }

        foreach (var c in t) {
            if (tDict.ContainsKey(c)) {
                tDict[c]++;
            } else {
                tDict[c] = 1;
            }
        }

        if (sDict.Count() != tDict.Count()) {
            return false;
        }

        foreach (var kvp in sDict) {
            if (!tDict.ContainsKey(kvp.Key) || tDict[kvp.Key] != kvp.Value) {
                return false;
            }
        }

        return true;
    }
}

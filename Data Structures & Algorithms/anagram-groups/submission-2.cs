public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var anagrams = new Dictionary<string, List<string>>();
        var res = new List<List<string>>();

        foreach (var str in strs) {
            var key = new string(str.OrderBy(c => c).ToArray());

            if (!anagrams.ContainsKey(key)) {
                anagrams[key] = new List<string>();
            }

            anagrams[key].Add(str);
        }

        foreach(var kvp in anagrams) {
            res.Add(kvp.Value);
        }

        return res;
    }
}

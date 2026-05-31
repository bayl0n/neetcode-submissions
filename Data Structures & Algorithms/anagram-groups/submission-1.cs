public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var res = new List<List<string>>();

        var anagrams = new Dictionary<string, List<string>>();

        foreach (var str in strs) {
            var strArray = str.ToCharArray();
            Array.Sort(strArray);

            var key = new string(strArray);

            if (!anagrams.ContainsKey(key)) {
                anagrams[key] = new List<string>();
            }
            anagrams[key].Add(str);
        }

        foreach ((var key, var value) in anagrams) {
            res.Add(value);
        }

        return res;
    }
}

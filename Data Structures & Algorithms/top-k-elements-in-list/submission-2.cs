public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var counts = new Dictionary<int, List<int>>();
        var frequencies = new Dictionary<int, int>();
        var res = new List<int>();

        foreach (var num in nums) {
            if (frequencies.ContainsKey(num)) {
                frequencies[num]++;
            } else {
                frequencies[num] = 1;
            }
        }

        foreach(var kvp in frequencies) {
            if (counts.ContainsKey(kvp.Value)) {
                counts[kvp.Value].Add(kvp.Key);
            } else {
                counts[kvp.Value] = new List<int>() { kvp.Key };
            }
        }

        for (var i = nums.Length; i >= 0; i--) {
            if (counts.ContainsKey(i)) {
                foreach (var num in counts[i]) {
                    res.Add(num);
                    if (res.Count >= k) {
                        return res.ToArray();
                    }
                }
            }
        } 

        return res.ToArray();
    }
}

public class Solution {
    public int LengthOfLongestSubstring(string s) {
        var left = 0;
        var charSet = new HashSet<char>();
        var maxCount = 0;

        for (var right = left; right < s.Length; right++) {
            while (charSet.Contains(s[right])) {
                charSet.Remove(s[left]);
                left++;
            }

            charSet.Add(s[right]);

            maxCount = Math.Max(maxCount, right - left + 1);
        }

        return maxCount;
    }
}

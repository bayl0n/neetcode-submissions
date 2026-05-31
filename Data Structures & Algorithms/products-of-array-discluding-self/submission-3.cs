public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        /*
            [1, 2, 4, 6]

            prefix array
            [1, 2, 8, 48]

            postfix array
            [1, 48, 24, 6]
        */

        var prefix = new List<int>();
        var postfix = new List<int>();
        var res = new List<int>();

        var curr = 1;
        foreach(var num in nums) {
            curr *= num;
            prefix.Add(curr);
        }

        curr = 1;
        for (var i = nums.Length-1; i >= 0; i--) {
            curr *= nums[i];
            postfix.Add(curr);
        }
        postfix.Reverse();

        for (var i = 0; i < nums.Length; i++) {
            var currRes = 1;

            if (i > 0) {
                currRes *= prefix[i-1];
            }

            if (i < nums.Length-1) {
                currRes *= postfix[i+1];
            }

            res.Add(currRes);
        }

        return res.ToArray();
    }
}

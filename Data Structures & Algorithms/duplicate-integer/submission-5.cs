public class Solution {
    public bool hasDuplicate(int[] nums) {
        /*
            Return TRUE if ANY value appears more than once.
            If no duplicates exist, then return FALSE.

            1, 2, 3, 3
            TRUE

            1, 2, 3, 4
            FALSE

            Is the given array sorted? No.

            -MAX_INT <= n <= MAX_INT

            Brute Force:
            Compare each element with each other (besides itself)
            and if they are equal to each other then we know we have
            a duplicate.

            for i in range(nums[::len(nums)-1]):
                for j in range(nums[i+1::]):
                    if nums[i] == nums[j]:
                        return True

            return False
        
        */

        // for (int i = 0; i < nums.Length; i++) {
        //     for (int j = i+1; j < nums.Length; j++) {
        //         if (nums[i] == nums[j]) {
        //             return true;
        //         }
        //     }
        // }

        // return false;

        /*
        Complexities:

        TC
        ---
        Since we are comparing n elements with each other, each
        element sees at least n elements, making the time complexity
        O(n)

        SC
        ---
        Since we are not taking any additional space that scales with
        n, it is constant (the variables i, j)
        O(1)
        */

        /*
        Can we get a more optimized solution?

        Yes. Instead of checking each element against each other, we can
        instead use a HashSet. With a HashSet, it ensures that each element
        that is inserted in it is unique. We can then verify if there is a duplicate
        by checking the length of the HashSet. If the lengths are not equal
        is no duplicate and we can return False. However, if the length of
        the HashSet is less than the length of the original array then we
        return True.
        */

        var numSet = new HashSet<int>();

        foreach (var num in nums) {
            numSet.Add(num);
        }

        return numSet.Count() < nums.Length;
    }
}

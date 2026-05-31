class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> num_set;

        for (auto num : nums) {
            num_set.emplace(num);
        }

        return num_set.size() != nums.size();
    }
};

class Solution {
public:
    bool isAnagram(string s, string t) {

        string sort_s = s;
        sort(sort_s.begin(), sort_s.end());

        string sort_t = t;
        sort(sort_t.begin(), sort_t.end());

        return sort_s == sort_t;
    }
};

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int m = 0;
        for (auto num: nums) {
            m = max(num, m);
        }
        int i = 0;
        int ret = 0;
        while (i < nums.size()) {
            int curr = 0;
            while (i < nums.size() && nums[i] == m) {
                curr++;
                i++;
            }
            ret = max(ret, curr);
            i++;
        }
        return ret;
    }
};

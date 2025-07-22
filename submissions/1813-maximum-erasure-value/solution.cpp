class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        vector<int> vals(10001, 0);
        int ret = 0;
        int count = 0;
        int left = 0;
        for (int i = 0; i < nums.size(); i++) {
            vals[nums[i]]++;
            count += nums[i];
            while(vals[nums[i]] > 1) {
                vals[nums[left]]--;
                count -= nums[left];
                left++;
            }
            ret = max(ret, count);
        }
        return ret;
    }
};

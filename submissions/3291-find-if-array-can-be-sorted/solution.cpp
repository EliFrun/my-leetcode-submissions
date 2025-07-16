class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        int bits = 0;
        int v = nums[0];
        while (v > 0) {
            if (v & 1) {
                bits += 1;
            }
            v >>= 1;
        }
        int start = 0;
        int prev_bits = bits;
        for (int i = 1; i < nums.size(); i++) {
            bits = 0;
            v = nums[i];
            while (v > 0) {
                if (v & 1) {
                    bits += 1;
                }
                v >>= 1;
            }
            if (bits != prev_bits) {
                sort(nums.begin() + start, nums.begin() + i);
                start = i;
                prev_bits = bits;
            }
        }

        sort(nums.begin() + start, nums.end());

        for (int i = 0; i < nums.size() - 1; i ++) {
            if (nums[i + 1] < nums[i]) {
                return false;
            }
        }
        return true;
    }
};

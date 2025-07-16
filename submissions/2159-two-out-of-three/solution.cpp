class Solution {
public:
    vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
        unordered_map<int, vector<int>> m = {};
        for (auto i: nums1) {
            if (m.find(i) == m.end()) {
                m[i] = {0, 0, 0};
            }
            m[i][0]++;
        }

        for (auto i: nums2) {
            if (m.find(i) == m.end()) {
                m[i] = {0, 0, 0};
            }
            m[i][1]++;
        }

        for (auto i: nums3) {
            if (m.find(i) == m.end()) {
                m[i] = {0, 0, 0};
            }
            m[i][2]++;
        }

        vector<int> ret = {};
        for (auto x: m) {
            int count = 0;
            for (int i: x.second) {
                if (i > 0) {
                    count++;
                }
            }
            if (count > 1) {
                ret.insert(ret.end(), x.first);
            }
        }

        return ret;
    }
};

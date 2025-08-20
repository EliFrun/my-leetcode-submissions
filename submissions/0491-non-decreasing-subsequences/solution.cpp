class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> ret;
        for (auto num: nums) {
            vector<vector<int>> new_ret;
            for (auto lis: ret) {
                new_ret.push_back(vector<int>(lis));
                if (lis.size() > 0 && lis[lis.size() - 1] <= num) {
                    lis.push_back(num);
                    new_ret.push_back(lis);
                }
            }
            new_ret.push_back({num});
            ret = new_ret;
        }
        vector<vector<int>> res;
        for (auto lis: ret) {
            if (lis.size() > 1) {
                res.push_back(lis);
            }
        }
        sort(res.begin(), res.end());
        res.erase(unique(res.begin(), res.end()), res.end());
        return res;
    }
};

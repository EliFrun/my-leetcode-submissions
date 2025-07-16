class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int, int> m= {};
        for (auto task: tasks) {
            if (m.find(task) == m.end()) {
                m[task] = 0;
            }
            m[task]++;
        }

        int ret = 0;
        for (auto v: m) {
            if (v.second == 1) {
                return -1;
            }
            ret += v.second % 3 == 0 ? int(v.second / 3) : int(v.second/3) + 1;
        }

        return ret;
    }
};

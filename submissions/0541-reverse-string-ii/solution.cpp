class Solution {
public:
    string reverseStr(string s, int k) {
        for (int i = 0; i < s.size(); i += k) {
            if (i / k & 1) {
                continue;
            } else {
                reverse(s.begin() + i, min(s.begin() + i + k, s.end()));
            }
        }
        return s;
    }
};

class Solution {
public:
    string makeFancyString(string s) {
        string ret = "";
        int count = 0;
        char curr = '-';
        for (auto c : s) {
            if (c == curr) {
                count += 1;
            } else {
                for (int i = 0; i < min(2, count); i ++) {
                    ret += curr;
                }
                curr = c;
                count = 1;
            }
        }
        for (int i = 0; i < min(2, count); i ++) {
            ret += curr;
        }
        return ret;
    }
};

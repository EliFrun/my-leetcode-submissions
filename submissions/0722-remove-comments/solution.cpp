class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        vector<string> ret = {};
        bool multi_line = false;
        string curr = "";
        for (auto st: source) {
            for (int i = 0; i < st.size(); i++) {
                if (!multi_line) {
                    if (i < st.size() - 1 && st[i] == '/' && st[i + 1] == '/') {
                        break;
                    } else if (i < st.size() - 1 && st[i] == '/' && st[i + 1] == '*') {
                        multi_line = true;
                        i++;
                    } else {
                        curr += st[i];
                    }
                } else {
                    if (i < st.size() - 1 && st[i] == '*' && st[i + 1] == '/') {
                        multi_line = false;
                        i++;
                    }
                }
            }
            if (!multi_line) {
                ret.insert(ret.end(), curr);
                curr = "";
            }
        }
        for (int i = ret.size() -1; i > -1; i -- ) {
            if (ret[i] == "") {
                ret.erase(ret.begin() + i);
            }
        }
        return ret;
    }
};

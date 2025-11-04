class Solution {
public:
    int maxRepeating(string sequence, string word) {
        vector<int> d = {};
        auto ret = 0;
        for (int i = 0; i < sequence.length(); i++){
            for (int j = d.size() - 1; j >= 0; j--) {
                if (sequence[i] == word[d[j] % word.length()]) {
                    d[j] += 1;
                    ret = max(ret, d[j]);
                } else {
                    d.erase(d.begin() + j);
                }
            }
            if (sequence[i] == word[0]) {
                d.push_back(1);
                ret = max(ret, 1);
            }
        }
        return ret / word.length();

    }
};

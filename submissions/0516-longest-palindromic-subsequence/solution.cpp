class Solution {
public:
    int lcs(vector<vector<int>> cache, string str1, string str2, int i, int j) {
        if (i >= str1.size()) {
            return 0;
        }

        if (j >= str2.size()) {
            return 0;
        }
        if (cache[i][j] >= 0) {
            return cache[i][j];
        }

        int ret = 0;
        if (str1[i] == str2[j]) {
            ret = 1 + lcs(cache, str1, str2, i + 1, j + 1);
        } else {
            int opt1 = lcs(cache, str1, str2, i + 1, j);
            int opt2 = lcs(cache, str1, str2, i, j + 1);
            ret = max(opt1, opt2);
        }
        cache[i][j] = ret;
        return ret;
    }

    int longestPalindromeSubseq(string s) {
        vector<vector<int>> cache = vector<vector<int>>(s.size());
        for (int i = 0; i < s.size(); i ++) {
            vector<int> lis = vector<int>(s.size());
            for (int j = 0; j < s.size(); j++) {
                lis[j] = 0;
            }
            cache[i] = lis;
        }

        for (int i = 0; i < s.size(); i ++) {
            for (int j = 0; j < s.size(); j++) {
                if (s[i] == s[s.size() - j - 1]) {
                    int v = 0;
                    if (i > 0 && j > 0) {
                        v = cache[i - 1][j - 1];
                    }
                    cache[i][j] = 1 + v;
                } else {    
                    int v1 = 0;
                    int v2 = 0;
                    if (i > 0){
                        v1 =  cache[i - 1][j];
                    }

                    if (j > 0) {
                        v2 = cache[i][j - 1];
                    }
                    cache[i][j] += max(v1, v2);
                }
            }
        }
        return cache[s.size() - 1][s.size() - 1];
    }
};

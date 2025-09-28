#define M 1000000007
class Solution {
public:
    vector<vector<long>> new_mat(int x) {
        vector<vector<long>> ret(x);
        for (int i = 0; i < x; i++) {
            ret[i] = vector<long>(x);
        }
        return ret;
    }
    vector<vector<long>> mat_mul(vector<vector<long>> m1, vector<vector<long>> m2) {
        auto ret = new_mat(m1.size());
        for (int i = 0; i < m1.size(); i++) {
            for (int j = 0; j < m1[0].size(); j++) {
                for (int k = 0; k < m1.size(); k++) {
                    ret[i][j] = (ret[i][j] + m1[i][k] * m2[k][j]) % M;
                }
            }
        }
        return ret;
    }
    
    int zigZagArrays(int n, int l, int r) {
        auto transition = new_mat(2 * (r - l + 1));
        for (int i = 0; i < transition.size(); i++) {
            for (int j = 0; j < transition.size(); j++) {
                if (j % 2 == 0 && i % 2 == 1 && i / 2 > j / 2) {
                    transition[i][j] = 1;
                }
                if (j % 2 == 1 && i % 2 == 0 && i / 2 < j / 2) {
                    transition[i][j] = 1;
                }
            }
        }

        n -= 1;
        auto ret = new_mat(2 * (r - l + 1));
        for (int i = 0; i < transition.size(); i ++) {
            ret[i][i] = 1;
        }
        while (n > 0) {
            if (n & 1) {
                ret = mat_mul(ret, transition);
            }
            transition = mat_mul(transition, transition);
            n >>= 1;
        }
        
        long res = 0;
        for (int i = 0; i < transition.size(); i++) {
            for (int j = 0; j < transition[0].size(); j++) {
                res = (res + ret[i][j]) % M;
            }
        }
        return res;

    }
};

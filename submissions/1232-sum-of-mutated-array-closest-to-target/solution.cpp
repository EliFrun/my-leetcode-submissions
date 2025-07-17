class Solution {
public:
    int findBestValue(vector<int>& arr, int target) {
        sort(arr.begin(), arr.end());
        int s = accumulate(arr.begin(), arr.end(), 0);
        int c = 0;

        if (target >= s) {
            return arr[arr.size() - 1];
        }

        for (int i = arr.size() - 1; i >= 0; i--) {
            if (i < arr.size() - 1 and arr[i] == arr[i + 1]) {
                c++;
                continue;
            }
            int min = s + arr[i] * c;
            int max = i < arr.size() - 1 ? s + arr[i + 1] * c : min;
            if (min <= target && target <= max) {
                int v = target - min;
                if (c == 0) {
                    return arr[i];
                }
                if (double(v) / c - int(v/c) <= 0.5) {
                    return arr[i] + int(double(v) / c);
                }
                return arr[i] + int(double(v) / c) + 1;
            }

            s -= arr[i];
            c += 1;
        }
        return double(target) / c - int(target/c) <= 0.5 ? int(target / c) : int(target / c) + 1;
    }
};

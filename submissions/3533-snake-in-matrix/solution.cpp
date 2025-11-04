class Solution {
public:
    int finalPositionOfSnake(int n, vector<string>& commands) {
        int x = 0, y = 0;
        map<string, pair<int, int>> m{
            {"UP", {0, -1}},
            {"DOWN", {0, 1}},
            {"LEFT", {-1, 0}},
            {"RIGHT", {1, 0}}
        };
        for (int i = 0; i < commands.size(); i++) {
            int dx = m[commands[i]].first;
            int dy = m[commands[i]].second;
            x += dx;
            y += dy;
        }
        return y * n + x;
    }
};

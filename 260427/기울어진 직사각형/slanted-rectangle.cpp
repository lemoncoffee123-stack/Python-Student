#include <iostream>
using namespace std;

int dr[] = {1, 1, -1, -1};
int dc[] = {1, -1, -1, 1};
int n, arr[20][20];
int start_r, start_c, ans = -1;

void dfs(int r, int c, int dir, int count) {
    for (int i = dir; i <= dir + 1 && i < 4; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (nr == start_r && nc == start_c && i == 3) {
            if (count > ans) ans = count;
            return;
        }

        if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
            dfs(nr, nc, i, count + arr[nr][nc]);
        }
    }
}


int main() {
    // Please write your code here.
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            start_r = i;
            start_c = j;

            int nr = start_r + dr[0];
            int nc = start_c + dc[0];

            if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                dfs(nr, nc, 0, arr[i][j] + arr[nr][nc]);
            }
        }
    }

    cout << ans;

    return 0;
}
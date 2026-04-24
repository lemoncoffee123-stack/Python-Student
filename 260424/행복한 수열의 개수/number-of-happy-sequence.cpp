#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n, m;
    cin >> n >> m;
    int arr[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    int total = 0;
    for (int i = 0; i < n; i++) {
        int cnt = 1, cursor = 0;
        bool is_find = false;
        for (int j = 0; j < n; j++) {
            if (arr[i][j] == cursor) {
                cnt += 1;
            }
            else if (cnt >= m) {
                is_find = true;
                break;
            }
            else {
                cnt = 1;
                cursor = arr[i][j];
            }
        }
        if (cnt >= m || is_find) {
            total += 1;
        }
    }

    for (int i = 0; i < n; i++) {
        int cnt = 1, cursor = 0;
        bool is_find = false;
        for (int j = 0; j < n; j++) {
            if (arr[j][i] == cursor) {
                cnt += 1;
            }
            else if (cnt >= m) {
                is_find = true;
                break;
            }
            else {
                cnt = 1;
                cursor = arr[j][i];
            }
        }
        if (cnt >= m || is_find) {
            total += 1;
        }
    }

    cout << total;
    return 0;
}
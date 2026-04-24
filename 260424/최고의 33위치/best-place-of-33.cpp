#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int arr[n][n];
    for (int i = 0; i < n; i++ ) {
        for (int j = 0; j <n; j++) {
            cin >> arr[i][j];
        }
    }

    int result = 0;
    for (int x = 0; x < n - 2; x++) {
        for (int y = 0; y < n - 2; y++) {
            int cnt = 0;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (arr[x + i][y + j] == 1) {
                        cnt += 1;
                    } 
                }
                if (result < cnt) result = cnt;
            }
        }
    }
    cout << result;
    return 0;
}
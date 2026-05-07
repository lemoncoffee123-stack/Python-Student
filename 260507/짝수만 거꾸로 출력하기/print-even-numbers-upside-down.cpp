#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int val, n, cnt = 0;
    cin >> n;
    int arr[n];
    for (int i=0; i<n; i++) {
        cin >> val;
        if (val % 2 == 0) {
            arr[cnt] = val;
            cnt++;
        }
    }
    for (int i=cnt-1; i>-1; i--) {
        cout << arr[i] << " ";
    }
    return 0;
}
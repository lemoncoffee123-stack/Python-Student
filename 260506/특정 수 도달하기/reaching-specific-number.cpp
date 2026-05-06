#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    int val, cnt = 0, total=0;
    for (int i=0; i<10; i++) {
        cin >> val;
        if (val >= 250) {
            if (cnt != 0) {
                cout << fixed;
                cout.precision(1);
                cout << total << " " << (double)total / cnt;
                break;
            }
            else {
                cout << 0 << " " << 0;
                break;
            }
        }
        else {
            cnt++;
            total += val;
        }
    }
    if (cnt == 10) {
        cout << fixed;
        cout.precision(1);
        cout << total << " " << (double)total/cnt;
    }
    return 0;
}
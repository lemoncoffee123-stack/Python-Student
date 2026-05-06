#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n, cnt=0;
    cin >> n;
    for (int i=0; i<n; i++) {
        int val, total=0;
        for (int j=0; j<4; j++) {
            cin >> val;
            total += val;
        }
        double avg;
        avg = (double)total / 4;

        if (avg >= 60) {
            cout << "pass" << endl;
            cnt++;
        }
        else {
            cout << "fail" << endl;
        }
    }
    cout << cnt;
    return 0;
}
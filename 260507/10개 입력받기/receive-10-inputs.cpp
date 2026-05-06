#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int val, total=0, cnt=0;
    for (int i=0; i<10; i++) {
        cin >> val;
        if (val == 0) {
            break;
        }
        total += val;
        cnt++;
    }
    cout << fixed;
    cout.precision(1);
    cout << total << " ";
    cout << (double)total / cnt;
    return 0;
}
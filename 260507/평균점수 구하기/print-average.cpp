#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    double val, total = 0;
    int cnt=0;
    for (int i=0; i<8; i++) {
        cin >> val;
        total += val;
        cnt++;
    }
    cout << fixed;
    cout.precision(1);
    cout << total / cnt;
    return 0;
}
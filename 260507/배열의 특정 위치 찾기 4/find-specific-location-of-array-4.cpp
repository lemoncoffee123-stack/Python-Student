#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int val, cnt=0, total=0;
    for (int i=0; i<10; i++) {
        cin >> val;
        if (val == 0) {
            break;
        }
        if (val % 2 == 0) {
            cnt++;
            total += val;
        }
    }
    cout << cnt << " " << total;
    return 0;
}
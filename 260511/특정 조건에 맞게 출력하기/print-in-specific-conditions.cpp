#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int val;
    for (int i=0; i<100; i++) {
        cin >> val;
        if (val == 0) {
            break;
        }
        else if (val % 2 == 0) {
            cout << val / 2 << " ";
        }
        else {
            cout << val + 3 << " ";
        }
    }
    return 0;
}
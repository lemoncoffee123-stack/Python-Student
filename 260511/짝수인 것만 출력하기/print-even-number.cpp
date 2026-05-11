#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n, val;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> val;
        if (val % 2 == 0) {
            cout << val << " ";
        }
    }
    return 0;
}
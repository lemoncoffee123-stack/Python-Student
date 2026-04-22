#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n, a;
    cin >> n;
    a = 1;
    for (int i = 1; i <= 100; i++) {
        a += i;
        if (a >= n) {
            cout << i;
            break;
        }
    }
    return 0;
}
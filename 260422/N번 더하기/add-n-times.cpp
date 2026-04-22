#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, n, i;
    cin >> a >> n;
    for (i = 0; i < n; i++) {
        cout << a + n << endl;
        a += n;
    }
    return 0;
}
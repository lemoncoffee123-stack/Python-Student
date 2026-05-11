#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n, cnt=0;
    cin >> n;
    int i = n;
    while (cnt < 2) {
        cout << i << " ";
        if (i % 5 == 0) {
            cnt++;
        }
        if (cnt == 2) {
            break;
        }
        i += n;
    }
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    while (true) {
        int a;
        cin >> a;
        if (a == 25) {
            cout << "Good" << endl;
            break;
        }

        if (a > 25) {
            cout << "Lower" << endl;
        }
        else cout << "Higher" << endl;
    }
    return 0;
}
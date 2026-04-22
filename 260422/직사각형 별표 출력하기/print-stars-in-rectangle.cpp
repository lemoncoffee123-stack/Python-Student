#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 2; j++) {
            cout << '*' << " ";
        }
        cout << "\n";
    }
    return 0;
}
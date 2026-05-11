#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char arr[10];
    for (int i=0; i<10; i++) {
        cin >> arr[i];
        if ((i + 2 ) % 3 == 0) {
            cout << arr[i] << " ";
        }
    }
    return 0;
}
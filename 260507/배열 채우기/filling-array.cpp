#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    int val, cnt = -1;
    for (int i=0; i<10; i++) {
        cin >> val;
        if (val == 0) {
            break;
        }
        cnt++;
        arr[i] = val;
    }
    for (int i=cnt; i>-1; i--) {
        cout << arr[i] << " ";
    }
    return 0;
}
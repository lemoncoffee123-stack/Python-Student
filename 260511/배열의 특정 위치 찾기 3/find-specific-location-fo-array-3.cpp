#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[100];
    int val, total=0;
    for (int i=0; i<100; i++) {
        cin >> val;
        arr[i] = val;
        if (val == 0) {
            for (int j=i; j>=i-3; j--) {
                total += arr[j];
            }
            break;
        }
    }
    cout << total;
    return 0;
}
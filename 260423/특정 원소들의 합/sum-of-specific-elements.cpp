#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[4][4];
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cin >> arr[i][j];
        }
    }

    int total = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j <= i; j++) {
            total += arr[i][j];
        }
    }
    cout << total;
    return 0;
}
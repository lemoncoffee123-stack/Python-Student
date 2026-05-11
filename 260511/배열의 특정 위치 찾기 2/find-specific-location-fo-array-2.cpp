#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    int total1=0,total2=0;

    for (int i=0; i<10; i++) {
        cin >> arr[i];
        if (i % 2 == 0) {
            total1 += arr[i];
        }
        if ((i + 1) % 2 == 0) {
            total2 += arr[i];
        }
    }
    if (total1 >= total2) {
        cout << total1 - total2;
    }
    else {
        cout << total2 - total1;
    }
    return 0;
}
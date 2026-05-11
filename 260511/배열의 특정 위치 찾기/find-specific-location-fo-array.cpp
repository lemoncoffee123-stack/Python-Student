#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    int val,total2=0,total3=0,cnt3=0;
    for (int i=0; i<10; i++) {
        cin >> val;
        arr[i] = val;
        if ((i + 1) % 2 == 0) {
            total2 += val;
        }
        if ((i + 1) % 3 == 0) {
            total3 += val;
            cnt3++;
        }
    }
    cout << fixed;
    cout.precision(1);
    cout << total2 << " " << (double)total3 / cnt3;
    return 0;
}
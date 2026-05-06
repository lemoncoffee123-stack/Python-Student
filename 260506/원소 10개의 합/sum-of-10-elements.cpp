#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int val,total=0;
    for (int i=0; i<10; i++) {
        cin >> val;
        total += val;
    }
    cout << total;
    return 0;
}
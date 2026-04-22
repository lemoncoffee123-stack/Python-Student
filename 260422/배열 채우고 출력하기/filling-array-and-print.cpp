#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char array[10];
    for (int i = 0; i < 10; i++) {
        cin >> array[i];
    }
 
    for (int i = 9; i > -1; i -= 1) {
        cout << array[i];
    }
    return 0;
}
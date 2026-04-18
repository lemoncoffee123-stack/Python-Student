#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a = 1;
    int b = 5;
    int c = 3;
    a = c;
    int d = a + c;
    int e = b - c;
    a = d;
    b = e;
    cout << a;
    cout <<'\n';
    cout << b;
    cout << '\n';
    cout << c;

    return 0;
}
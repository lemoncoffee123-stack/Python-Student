#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string a;
    cin >> a;
    int len = a.length();
    a[1] = 'a';
    a[len - 2] = 'a';
    cout << a;
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c;
    cin >> a >> b >> c;
    int total = a + b + c;
    int average = total / 3;
    cout << total << endl ;
    cout << average << endl;
    cout << total - average;
    return 0;
}
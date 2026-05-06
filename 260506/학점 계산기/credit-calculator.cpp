#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    double val, total=0;
    for (int i=0; i<n; i++) {
        cin >> val;
        total += val;
    }
    double avg = total / n;
    cout << fixed;
    cout.precision(1);
    cout << avg << endl;
    if (avg >= 4.0) {
        cout << "Perfect";
    }
    else if (avg >= 3.0) {
        cout << "Good";
    }
    else {
        cout << "Poor";
    }
    return 0;
}
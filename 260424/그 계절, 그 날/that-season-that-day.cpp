#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int y, m, d;
    cin >> y >> m >> d;
    bool is_yun, is_impossible;
    is_yun = false;
    if (y % 4 == 0 ) {
        if (y % 100 == 0) {
            if (y % 400 == 0) {
                is_yun = true;
            }
        }
        else is_yun = true;
    }
    is_impossible = false;
    if (m == 2) {
        if (is_yun && d > 30) {
            is_impossible = true;
        }
    }

    if (m < 1 || m > 12) is_impossible = true;
    else {
        if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) {
            if (d > 31) is_impossible = true;
        }
        else {
            if (d > 30) is_impossible = true;
        }
    }

    if (is_impossible) {
        cout << -1;
    }
    else {
        if (m >= 3 && m <= 5) cout << "Spring";
        else if (m >= 6 && m <= 8) cout << "Summer";
        else if (m >= 9 && m <= 11) cout << "Fall";
        else cout << "Winter";
    }
    return 0;
}
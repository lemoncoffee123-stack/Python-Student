#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;
    int prime[11] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
    int prime_squre[11];
    for (int i = 0; i < 11; i++) {
        prime_squre[i] = prime[i] * prime[i];
    }
    int cnt = 0;
    for (int i = 0; i < 11; i++) {
        if (prime_squre[i] >= a && prime_squre[i] <= b) cnt += 1;
    }

    cout << cnt;
    return 0;
}
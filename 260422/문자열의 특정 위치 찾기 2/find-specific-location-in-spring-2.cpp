#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char a;
    cin >> a;
    string arr[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    int cnt = 0;
    for (int i = 0; i < 5; i++) {
        string word = arr[i];
        if (word[2] == a || word[3] == a) {
            cnt += 1;
            cout << word << endl;
        }
    }
    cout << cnt;
    return 0;
}
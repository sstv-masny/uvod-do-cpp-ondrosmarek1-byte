
#include <iostream>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    unsigned long long n;
    if (!(std::cin >> n))
        return 0;
    unsigned long long rev = 0;
    if (n == 0) {
        std::cout << "0";
        return 0;
    }
    while (n > 0) {
        rev = rev * 10 + n % 10;
        n = n / 10;
    }
    std::cout << rev;
    return 0;
}

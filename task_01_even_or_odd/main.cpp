
#include <iostream>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    long long n; // zadefinujeme premennu
    if (!(std::cin >> n))
        return 0;
    if (n % 2 == 0) { // testujeme delitelnost 2
        std::cout << "even";
    } else {
        std::cout << "odd";
    }
    return 0;
}

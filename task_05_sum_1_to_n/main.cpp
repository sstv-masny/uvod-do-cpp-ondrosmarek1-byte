
#include <iostream>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    long long n;
    if (!(std::cin >> n))
        return 0;
    long long sucet = 0;
    while (n > 0) {
        sucet = sucet + n;
        n = n - 1;
    }
    std::cout << sucet;
    return 0;
}

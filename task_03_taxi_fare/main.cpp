
#include <cmath>
#include <iomanip>
#include <iostream>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    long long k;
    if (!(std::cin >> k))
        return 0;
    double fare;
    if (k <= 2) {
        fare = 4.00;
    } else
        fare = 4.00 + 1.50 * ceil(k - 2.00);
    std::cout << std::fixed << std::setprecision(2) << fare;
    return 0;
}

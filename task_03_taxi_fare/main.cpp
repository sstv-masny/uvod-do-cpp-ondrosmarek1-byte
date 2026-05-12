
#include <iostream>
#include <iomanip>
#include <cmath>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    long long k;
    if (!(std::cin >> k)) return 0;         
    double fare = 3.0 + 2.0 * std::ceil(k / 1400.0); //tuto ulohu by som si chcel pozriet
    std::cout << std::fixed << std::setprecision(2) << fare << "\n";
    return 0;
}

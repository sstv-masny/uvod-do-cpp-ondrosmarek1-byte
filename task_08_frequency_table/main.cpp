#include <iostream>
#include <vector>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    if (!(std::cin >> n))
        return 0;
    std::vector<long long> a(n);
    for (int i = 0; i < n; i++)
        std::cin >> a[i];
    long long x;
    std::cin >> x;
    int najv = n - 1, najn = 0;
    int mid = a.size() / 2;
    int location = -1;
    while (najn <= najv) {
        mid = (najv + najn) / 2;
        if (a[mid] < x) {
            najn = mid + 1;
        } else if (a[mid] > x) {
            najv = mid - 1;
        } else if (a[mid] == x) {
            location = mid;
            najv = mid - 1;
        }
    }

    std::cout << location;
    return 0;
}
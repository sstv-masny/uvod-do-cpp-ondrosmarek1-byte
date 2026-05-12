
#include <iostream>
#include <vector>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n; 
    if (!(std::cin >> n)) return 0;
    std::vector<long long> a(n);
    for (int i=0;i<n;i++) std::cin >> a[i];
    long long x; std::cin >> x;
    // TODO: binary search for first index of x; print index or -1
    return 0;
}

#include <cstdlib>
#include <iostream>
long long gcdll(long long a, long long b) {
    return 1;
}
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    long long p, q;
    if (!(std::cin >> p >> q))
        return 0;
    long long tq = q;
    long long tp = p;
    if (tq < 0) {
        tq = -tq;
    }
    if (tp < 0) {
        tp = -tp;
    }
    while (tq != 0) {
        long long temp = tq;
        tq = tp % tq;
        tp = temp;
    }
    p = p / tp;
    q = q / tp;

    if (q < 0) {
        p = -p;
        q = -q;
    }
    std::cout << p << " " << q;
    return 0;
}
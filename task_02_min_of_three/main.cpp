
#include <iostream>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    long long a,b,c;
    if (!(std::cin >> a >> b >> c)) return 0;
    long long min = a;      //zadefinujeme "a" ako minimum
    if (b < min) min = b;  //testujeme ci b alebo c niesu mensie nez definovane minimum
    if (c < min) min = c;
    std::cout << min << "\n";
    return 0;
}

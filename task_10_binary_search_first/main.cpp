#include <cctype>
#include <iostream>
#include <string>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::string s;
    if (!std::getline(std::cin, s))
        return 0;
    std::string rs;
    std::string cs = "";
    for (int i = 0; i < s.length(); i++) {
        s[i] = std::tolower(s[i]);
    }
    for (int i = 0; i < s.length(); i++) {
        if (s[i] >= 'a' && s[i] <= 'z') {
            cs = cs + s[i];
        }
    }
    for (int i = cs.size() - 1; i >= 0; i--) {
        rs = rs + cs[i];
    }
    std::cout << (cs == rs ? "YES" : "NO");
    return 0;
}
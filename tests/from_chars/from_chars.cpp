// Test case from rhbz#1657544

#include <charconv>
#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char **argv)
{
    size_t r=0;
    const char *begin = argv[1];
    const char *end = begin + strlen(begin);
    from_chars(begin, end, r);
    cout << r << '\n';
    return 0;
}

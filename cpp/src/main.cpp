#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main()
{
    cout << "Hello, World!" << endl;
    cout << "What\'s your name? " << endl;
    char name[50];
    cin >> name;
    cout << "Your name is: " << name << "?" << endl;

    return 0;
}

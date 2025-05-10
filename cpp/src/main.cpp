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

void data_types()
{
    /***************************
     *   Integer types
     ***************************/
    // unsigned short
    unsigned short int exam_score{55};
    cout << "My exam score was " << exam_score << endl;

    // signed int
    int countries_represented{65};
    cout << "There were " << countries_represented << " countries represented in my meeting!" << endl;

    // signed long int
    long people_in_florida{20610000};
    cout << "There are about " << people_in_florida << " people in Florida!" << endl;

    // signed long long int
    long long people_on_earth{8'000'000'000};
    cout << "There are about " << people_on_earth << " people on earth!" << endl;

    /***************************
     *   Floating point types
     ***************************/
    float car_payment{401.23};
    cout << "My car payment is " << car_payment << endl;

    double pi{3.14159};
    cout << "Pi is" << pi << endl;

    long double large_amount{2.7e120};
    cout << large_amount << "is a very big number!" << endl;

    /***************************
     *   Boolean types
     ***************************/
    bool gameOver{false};
    cout << "The value of gameOver is " << gameOver << endl;

    /***************************
     *   Overflow example
     ***************************/
    short value1{30000};
    short value2{1000};
    short sum{value1 * value2};
    cout << "The sum of " << value1 << " and " << value2 << " is " << sum << endl;
}

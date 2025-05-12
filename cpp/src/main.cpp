#include <iostream>

using std::cin;
using std::cout;
using std::endl;

void hello_world();
void data_types();
void data_types_sizes();
void arrays();
void consts();

int main()
{
    hello_world();
    data_types();
    data_types_sizes();
    arrays();
    consts();

    return 0;
}

void hello_world()
{
    cout << "Hello, World!" << endl;
    cout << "What\'s your name? " << endl;
    char name[50];
    cin >> name;
    cout << "Your name is: " << name << "?" << endl;
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

void data_types_sizes()
{
    cout << "The size of char is: " << sizeof(char) << endl;
    cout << "The size of short int is: " << sizeof(short int) << endl;
    cout << "The size of int is: " << sizeof(int) << endl;
    cout << "The size of unsigned int is: " << sizeof(unsigned int) << endl;
    cout << "The size of long int is: " << sizeof(long int) << endl;
    cout << "The size of long long int is: " << sizeof(long long int) << endl;
    cout << "The size of float is: " << sizeof(float) << endl;
    cout << "The size of double is: " << sizeof(double) << endl;
    cout << "The size of long double is: " << sizeof(long double) << endl;
}

void arrays()
{
    int my_nums[10]{};
    my_nums[0] = 10;
    my_nums[1] = 320;
    my_nums[2] = 405;
    my_nums[3] = 595;
    my_nums[4] = 610;
    my_nums[5] = 740;
    my_nums[6] = 890;
    my_nums[7] = 12000;
    my_nums[8] = 20500;
    my_nums[9] = 190230;
    cout << my_nums << endl;
    cout << my_nums[0] << endl;
    cout << my_nums[1] << endl;
    cout << my_nums[2] << endl;
    cout << my_nums[3] << endl;
    cout << my_nums[4] << endl;
    cout << my_nums[5] << endl;
    cout << my_nums[6] << endl;
    cout << my_nums[7] << endl;
    cout << my_nums[8] << endl;
    cout << my_nums[9] << endl;
}

void consts()
{
  const int my_age {21};
  cout << "My age is " << my_age << " and will be it forever!" << endl;
  cout << "At least i hope..." << endl;
}

#include <stdio.h>

enum Company
{
    GOOGLE,
    FACEBOOK,
    XEROX,
    YAHOO,
    EBAY,
    MICROSOFT
};

enum Months
{
    January,
    February,
    March,
    April,
    May,
    June,
    July,
    August,
    September,
    October,
    November,
    December
} Months;

enum Colors
{
    red,
    blue,
    yellow
};

int main()
{
    printf("================Companies================\n");
    printf("Companies in the order the teacher asked:\n");
    printf("Xerox: %d\n", XEROX);
    printf("Google: %d\n", GOOGLE);
    printf("Ebay: %d\n", EBAY);
    printf("Companies in the right order:\n");
    printf("Google: %d\n", GOOGLE);
    printf("Facebook: %d\n", FACEBOOK);
    printf("Xerox: %d\n", XEROX);
    printf("Yahoo: %d\n", YAHOO);
    printf("Ebay: %d\n", EBAY);
    printf("Microsoft: %d\n", MICROSOFT);
    printf("=========================================\n");
    return 0;
}

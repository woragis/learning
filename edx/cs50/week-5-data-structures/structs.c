#include <stdio.h>
#include <stdlib.h>

typedef struct CAR
{
    int year;
    char* plate;
} CAR;

int main(void)
{

    CAR mycar;
    mycar.year = 2025;
    mycar.plate = "Jezreel";
    CAR* collection[3];
    collection[0]->year = 2023;
    collection[0]->plate= "Jezreel";
    collection[1]->year = 2023;
    collection[1]->plate = "Jezreel";
    collection[2]->year = 2023;
    collection[2]->plate = "Jezreel";
    printf("Car: '%s' - year: '%i'\n", mycar.plate, mycar.year);


    // Variable declaration
    struct CAR *secondCar = malloc(sizeof(struct CAR));
    return 0;
}

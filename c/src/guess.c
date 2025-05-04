#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

void start_menu();
void choice_menu(int *range);
void main_loop(int *guesses, int *random_number, int *guess);

int main()
{

    // Start menu
    start_menu();

    // Choice menu show up
    int range;
    choice_menu(&range);

    int guesses = 8;
    int guess;

    // Bot random number
    time_t t;
    srand((unsigned)time(&t));
    int random_number = 0;
    random_number = rand() % range;

    // Game Mainloop
    main_loop(&guesses, &random_number, &guess);

    return 0;
}

void start_menu()
{
    printf("===========================================\n");
    printf("=-=-=-=-=-=-=-=-Guessing Game-=-=-=-=-=-=-=\n");
    printf("===========================================\n");
    printf("============Guess a random number==========\n");
    printf("===========================================\n");
}

void choice_menu(int *range)
{
    printf("What range do you want to play?\n");
    scanf("%d", &(*range));
    printf("Okay, the range %d was chosen\n", *range);
}

void main_loop(int *guesses, int *random_number, int *guess)
{
    while (*guesses > 0 && *random_number != *guess)
    {
        printf("You have %d guesses left!\n", *guesses);
        scanf("%d", &(*guess));
        if (*guess > *random_number)
        {
            printf("Too high\n");
        }
        else if (*guess < *random_number)
        {
            printf("Too low\n");
        }
        else
        {
            printf("You guessed it right, the bot number was %d\n", *random_number);
        }
        (*guesses)--;
    }
}
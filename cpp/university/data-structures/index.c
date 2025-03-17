#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CONTACTS 100
#define MAX_USERS 100
#define NAME_LENGTH 50
#define PHONE_LENGTH 12

typedef struct
{
    char name[NAME_LENGTH];
    char phone[PHONE_LENGTH];
} Contact;

typedef struct
{
    char username[NAME_LENGTH];
    Contact contacts[MAX_CONTACTS];
    int contact_count;
} User;

typedef struct
{
    User users[MAX_USERS];
    int user_count;
} UserDatabase;

void interaction_control();
int get_user(User *user);

int main()
{
    User user;
    // GET USERNAME

    // Show question
    printf("What\'s your name? ");

    // Get Input
    fgets(user.username, NAME_LENGTH, stdin);
    // Remove newline from string
    user.username[strcspn(user.username, "\n")] = 0;
    // interaction_control();
    // User *user = NULL;
    // get_user(user);
    // UserDatabase db = {.user_count = 0};
    // User me = {.username = "Jezreel", .contact_count = 0, .contacts = {}};
    // Contact first_contact = {.name = "jezreel", .phone = "839969128879"};

    // // Modifying strings example
    // printf("Name before: '%s'\n", first_contact.name);
    // strcpy(first_contact.name, "Not jezreel anymore");
    // printf("Name after: '%s'\n", first_contact.name);
    // printf("Phone number: '%s'\n", first_contact.phone);

    // Contact second_contact = {.name = "", .phone = ""};
    // printf("Second contact\n");
    // printf("Name Before: '%s'\n", second_contact.name);

    // // Get input
    // fgets(second_contact.name, NAME_LENGTH, stdin);

    // // Remove \n from new string
    // second_contact.name[strcspn(second_contact.name, "\n")] = 0;
    // printf("Name After: '%s'\n", second_contact.name);
}

// void register_user(User *new_user)
// {
//     get_user(new_user);
//     printf("User name: '%s'", new_user->username);
//     return;
// }

User *login_user() {}

int get_user(User *user)
{
    return 1;
}

void interaction_control()
{
    int choice;
    while (1)
    {
        printf("\n======================\n");
        printf("Choose your action:\n");
        printf("======================\n");
        printf("1. Create user\n");
        printf("2. Login user\n");
        printf("3. Add contact (must be logged in)\n");
        printf("4. Search contact (must be logged in)\n");
        printf("5. Exit\n");
        printf("Enter a choice: ");

        scanf("%d", choice);
        getchar();

        switch (choice)
        {
        case 1:
            break;
        case 2:
            break;
        case 5:
            printf("Exiting...");
            return;
            break;

        default:
            break;
        }
    }
    return;
}

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

int main()
{
    // UserDatabase db = {.user_count = 0};
    // User me = {.username = "Jezreel", .contact_count = 0, .contacts = {}};
    Contact first_contact = {.name = "jezreel", .phone = "839969128879"};

    // Modifying strings example
    printf("Name before: '%s'\n", first_contact.name);
    strcpy(first_contact.name, "Not jezreel anymore");
    printf("Name after: '%s'\n", first_contact.name);
    printf("Phone number: '%s'\n", first_contact.phone);
}
#include <stdio.h>
#include <string.h>

#define MAX_CONTACTS 100
#define NAME_LENGTH 50
#define PHONE_LENGTH 15

typedef struct {
    char name[NAME_LENGTH];
    char phone[PHONE_LENGTH];
} Contact;

typedef struct {
    Contact contacts[MAX_CONTACTS];
    int contact_count;
} User;

void add_contact(User *user, const char *name, const char *phone) {
    if (user->contact_count < MAX_CONTACTS) {
        strncpy(user->contacts[user->contact_count].name, name, NAME_LENGTH - 1);
        user->contacts[user->contact_count].name[NAME_LENGTH - 1] = '\0';
        strncpy(user->contacts[user->contact_count].phone, phone, PHONE_LENGTH - 1);
        user->contacts[user->contact_count].phone[PHONE_LENGTH - 1] = '\0';
        user->contact_count++;
    } else {
        printf("Contact list is full!\n");
    }
}

Contact *search_contact_by_name(User *user, const char *name) {
    for (int i = 0; i < user->contact_count; i++) {
        if (strcmp(user->contacts[i].name, name) == 0) {
            return &user->contacts[i];
        }
    }
    return NULL;
}

Contact *search_contact_by_index(User *user, int index) {
    if (index >= 0 && index < user->contact_count) {
        return &user->contacts[index];
    }
    return NULL;
}

void print_contact(Contact *contact) {
    if (contact) {
        printf("Name: %s, Phone: %s\n", contact->name, contact->phone);
    } else {
        printf("Contact not found!\n");
    }
}

int main() {
    User user = {.contact_count = 0};
    
    add_contact(&user, "Alice", "1234567890");
    add_contact(&user, "Bob", "0987654321");
    
    printf("Search by name: \n");
    print_contact(search_contact_by_name(&user, "Alice"));
    
    printf("Search by index: \n");
    print_contact(search_contact_by_index(&user, 1));
    
    return 0;
}

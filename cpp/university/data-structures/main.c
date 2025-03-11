#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <jansson.h>

#define MAX_CONTACTS 100
#define NAME_LENGTH 50
#define PHONE_LENGTH 15
#define FILENAME "user_data.json"

typedef struct {
    char name[NAME_LENGTH];
    char phone[PHONE_LENGTH];
} Contact;

typedef struct {
    char username[NAME_LENGTH];
    Contact contacts[MAX_CONTACTS];
    int contact_count;
} User;

void save_user_to_json(User *user) {
    json_t *root = json_object();
    json_object_set_new(root, "username", json_string(user->username));
    json_t *contacts_array = json_array();

    for (int i = 0; i < user->contact_count; i++) {
        json_t *contact = json_object();
        json_object_set_new(contact, "name", json_string(user->contacts[i].name));
        json_object_set_new(contact, "phone", json_string(user->contacts[i].phone));
        json_array_append_new(contacts_array, contact);
    }

    json_object_set_new(root, "contacts", contacts_array);
    json_dump_file(root, FILENAME, JSON_INDENT(4));
    json_decref(root);
}

void load_user_from_json(User *user) {
    json_t *root;
    json_error_t error;
    root = json_load_file(FILENAME, 0, &error);
    if (!root) {
        printf("No existing user data found.\n");
        return;
    }
    
    json_t *username = json_object_get(root, "username");
    json_t *contacts_array = json_object_get(root, "contacts");
    
    strncpy(user->username, json_string_value(username), NAME_LENGTH - 1);
    user->contact_count = json_array_size(contacts_array);
    
    for (int i = 0; i < user->contact_count; i++) {
        json_t *contact = json_array_get(contacts_array, i);
        json_t *name = json_object_get(contact, "name");
        json_t *phone = json_object_get(contact, "phone");
        
        strncpy(user->contacts[i].name, json_string_value(name), NAME_LENGTH - 1);
        strncpy(user->contacts[i].phone, json_string_value(phone), PHONE_LENGTH - 1);
    }
    json_decref(root);
}

void create_user(User *user) {
    printf("Enter username: ");
    fgets(user->username, NAME_LENGTH, stdin);
    user->username[strcspn(user->username, "\n")] = 0;
    user->contact_count = 0;
    save_user_to_json(user);
    printf("User created successfully!\n");
}

void add_contact(User *user) {
    if (user->contact_count < MAX_CONTACTS) {
        printf("Enter contact name: ");
        fgets(user->contacts[user->contact_count].name, NAME_LENGTH, stdin);
        user->contacts[user->contact_count].name[strcspn(user->contacts[user->contact_count].name, "\n")] = 0;
        
        printf("Enter contact phone: ");
        fgets(user->contacts[user->contact_count].phone, PHONE_LENGTH, stdin);
        user->contacts[user->contact_count].phone[strcspn(user->contacts[user->contact_count].phone, "\n")] = 0;
        
        user->contact_count++;
        save_user_to_json(user);
        printf("Contact added successfully!\n");
    } else {
        printf("Contact list is full!\n");
    }
}

void search_contact(User *user) {
    char search_name[NAME_LENGTH];
    printf("Enter name to search: ");
    fgets(search_name, NAME_LENGTH, stdin);
    search_name[strcspn(search_name, "\n")] = 0;

    for (int i = 0; i < user->contact_count; i++) {
        if (strcmp(user->contacts[i].name, search_name) == 0) {
            printf("Contact found - Name: %s, Phone: %s\n", user->contacts[i].name, user->contacts[i].phone);
            return;
        }
    }
    printf("Contact not found.\n");
}

void display_user(User *user) {
    printf("User: %s\n", user->username);
    printf("Contacts:\n");
    for (int i = 0; i < user->contact_count; i++) {
        printf("%d. Name: %s, Phone: %s\n", i + 1, user->contacts[i].name, user->contacts[i].phone);
    }
}

int main() {
    User user = {.contact_count = 0};
    load_user_from_json(&user);
    int choice;
    
    while (1) {
        printf("\nMenu:\n");
        printf("1. Login (Create User)\n");
        printf("2. Add Contact\n");
        printf("3. Search Contact\n");
        printf("4. Display User\n");
        printf("5. Exit\n");
        printf("Enter choice: ");
        
        scanf("%d", &choice);
        getchar(); // Clear newline from input buffer
        
        switch (choice) {
            case 1:
                create_user(&user);
                break;
            case 2:
                add_contact(&user);
                break;
            case 3:
                search_contact(&user);
                break;
            case 4:
                display_user(&user);
                break;
            case 5:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice. Try again.\n");
        }
    }
}

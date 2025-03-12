#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <jansson.h>

#define MAX_CONTACTS 100
#define MAX_USERS 100
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

typedef struct {
    User users[MAX_USERS];
    int user_count;
} UserDatabase;

void save_users_to_json(UserDatabase *db) {
    json_t *root = json_array();
    
    for (int i = 0; i < db->user_count; i++) {
        json_t *user_obj = json_object();
        json_object_set_new(user_obj, "username", json_string(db->users[i].username));
        json_t *contacts_array = json_array();
        
        for (int j = 0; j < db->users[i].contact_count; j++) {
            json_t *contact_obj = json_object();
            json_object_set_new(contact_obj, "name", json_string(db->users[i].contacts[j].name));
            json_object_set_new(contact_obj, "phone", json_string(db->users[i].contacts[j].phone));
            json_array_append_new(contacts_array, contact_obj);
        }
        
        json_object_set_new(user_obj, "contacts", contacts_array);
        json_array_append_new(root, user_obj);
    }
    
    json_dump_file(root, FILENAME, JSON_INDENT(4));
    json_decref(root);
}

void load_users_from_json(UserDatabase *db) {
    json_t *root;
    json_error_t error;
    root = json_load_file(FILENAME, 0, &error);
    if (!root) {
        printf("No existing user data found.\n");
        return;
    }
    
    db->user_count = json_array_size(root);
    for (int i = 0; i < db->user_count; i++) {
        json_t *user_obj = json_array_get(root, i);
        json_t *username = json_object_get(user_obj, "username");
        json_t *contacts_array = json_object_get(user_obj, "contacts");
        
        strncpy(db->users[i].username, json_string_value(username), NAME_LENGTH - 1);
        db->users[i].contact_count = json_array_size(contacts_array);
        
        for (int j = 0; j < db->users[i].contact_count; j++) {
            json_t *contact_obj = json_array_get(contacts_array, j);
            json_t *name = json_object_get(contact_obj, "name");
            json_t *phone = json_object_get(contact_obj, "phone");
            
            strncpy(db->users[i].contacts[j].name, json_string_value(name), NAME_LENGTH - 1);
            strncpy(db->users[i].contacts[j].phone, json_string_value(phone), PHONE_LENGTH - 1);
        }
    }
    json_decref(root);
}

void register_user(UserDatabase *db) {
    if (db->user_count < MAX_USERS) {
        printf("Enter new username: ");
        fgets(db->users[db->user_count].username, NAME_LENGTH, stdin);
        db->users[db->user_count].username[strcspn(db->users[db->user_count].username, "\n")] = 0;
        db->users[db->user_count].contact_count = 0;
        db->user_count++;
        save_users_to_json(db);
        printf("User registered successfully!\n");
    } else {
        printf("User database is full!\n");
    }
}

User *login(UserDatabase *db) {
    char username[NAME_LENGTH];
    printf("Enter username to login: ");
    fgets(username, NAME_LENGTH, stdin);
    username[strcspn(username, "\n")] = 0;
    
    for (int i = 0; i < db->user_count; i++) {
        if (strcmp(db->users[i].username, username) == 0) {
            printf("Login successful!\n");
            return &db->users[i];
        }
    }
    printf("User not found.\n");
    return NULL;
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
        printf("Contact added successfully!\n");
    } else {
        printf("Contact list is full!\n");
    }
}

void display_user(User *user) {
    printf("User: %s\n", user->username);
    printf("Contacts:\n");
    for (int i = 0; i < user->contact_count; i++) {
        printf("%d. Name: %s, Phone: %s\n", i + 1, user->contacts[i].name, user->contacts[i].phone);
    }
}

int main() {
    UserDatabase db = {.user_count = 0};
    load_users_from_json(&db);
    User *current_user = NULL;
    int choice;
    
    while (1) {
        printf("\nMenu:\n");
        printf("1. Register User\n");
        printf("2. Login\n");
        printf("3. Add Contact\n");
        printf("4. Display User\n");
        printf("5. Exit\n");
        printf("Enter choice: ");
        
        scanf("%d", &choice);
        getchar(); // Clear newline from input buffer
        
        switch (choice) {
            case 1:
                register_user(&db);
                break;
            case 2:
                current_user = login(&db);
                break;
            case 3:
                if (current_user) {
                    add_contact(current_user);
                    save_users_to_json(&db);
                } else {
                    printf("Please login first.\n");
                }
                break;
            case 4:
                if (current_user) {
                    display_user(current_user);
                } else {
                    printf("Please login first.\n");
                }
                break;
            case 5:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice. Try again.\n");
        }
    }
}

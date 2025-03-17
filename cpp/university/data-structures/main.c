//
// Projeto criado com o fim de salvar contatos
//
// Funcionalidades:
//  1. Adicionar contato
//  2. Procurar contato por nome
//  3. Procurar contato por indice
//  4. Dados sao salvos persistentemente em forma de binario
//
// Autor: Jezreel de Andrade
// Linkedin: https://www.linkedin.com/in/jezreel-andrade/
// Github: https://github.com/woragis
// Github do Projeto: https://github.com/woragis/learning/blob/main/cpp/university/data-structures/main.c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_CONTACTS 100
#define NAME_LENGTH 50
#define PHONE_LENGTH 15
#define FILE_NAME "contacts.dat"

// Estrutura para armazenar um contato
typedef struct
{
    char name[NAME_LENGTH];
    char phone[PHONE_LENGTH];
} Contact;

// Estrutura para armazenar a lista de contatos
typedef struct
{
    Contact contacts[MAX_CONTACTS];
    int contact_count;
} User;

// Função para salvar os contatos em um arquivo binário
void save_contacts(User *user)
{
    FILE *file = fopen(FILE_NAME, "wb");
    if (!file)
    {
        printf("Erro ao salvar os contatos!\n");
        return;
    }
    fwrite(user, sizeof(User), 1, file);
    fclose(file);
}

// Função para carregar os contatos do arquivo binário
void load_contacts(User *user)
{
    FILE *file = fopen(FILE_NAME, "rb");
    if (!file)
    {
        printf("Nenhum contato salvo encontrado. Criando nova lista.\n");
        return;
    }
    fread(user, sizeof(User), 1, file);
    fclose(file);
}

// Função para adicionar um novo contato
void add_contact(User *user)
{
    if (user->contact_count >= MAX_CONTACTS)
    {
        printf("Lista de contatos está cheia!\n");
        return;
    }

    // Captura do nome do contato
    printf("Digite o nome: ");
    fgets(user->contacts[user->contact_count].name, NAME_LENGTH, stdin);
    user->contacts[user->contact_count].name[strcspn(user->contacts[user->contact_count].name, "\n")] = '\0';

    // Captura do telefone do contato
    printf("Digite o telefone: ");
    fgets(user->contacts[user->contact_count].phone, PHONE_LENGTH, stdin);
    user->contacts[user->contact_count].phone[strcspn(user->contacts[user->contact_count].phone, "\n")] = '\0';

    user->contact_count++;
    save_contacts(user); // Salva os contatos após adicionar
    printf("Contato adicionado com sucesso!\n");
}

// Função para buscar um contato pelo nome
void search_contact_by_name(User *user)
{
    char name[NAME_LENGTH];
    printf("Digite o nome a buscar: ");
    fgets(name, NAME_LENGTH, stdin);
    name[strcspn(name, "\n")] = '\0';

    for (int i = 0; i < user->contact_count; i++)
    {
        if (strcmp(user->contacts[i].name, name) == 0)
        {
            printf("Contato encontrado: Nome: %s, Telefone: %s\n", user->contacts[i].name, user->contacts[i].phone);
            return;
        }
    }
    printf("Contato não encontrado!\n");
}

// Função para buscar um contato pelo índice
void search_contact_by_index(User *user)
{
    int index;
    char buffer[10];
    printf("Digite o índice do contato: ");
    fgets(buffer, sizeof(buffer), stdin);
    sscanf(buffer, "%d", &index);

    if (index >= 0 && index < user->contact_count)
    {
        printf("Contato encontrado: Nome: %s, Telefone: %s\n", user->contacts[index].name, user->contacts[index].phone);
    }
    else
    {
        printf("Índice inválido!\n");
    }
}

int main()
{
    User user = {.contact_count = 0};
    load_contacts(&user); // Carrega os contatos ao iniciar o programa
    int option;
    char buffer[10];

    do
    {
        // Exibição do menu de opções
        printf("\nMenu:\n");
        printf("1. Adicionar contato\n");
        printf("2. Buscar contato por nome\n");
        printf("3. Buscar contato por índice\n");
        printf("4. Sair\n");
        printf("Escolha uma opção: ");
        fgets(buffer, sizeof(buffer), stdin);
        sscanf(buffer, "%d", &option);

        // Execução da opção escolhida
        switch (option)
        {
        case 1:
            add_contact(&user);
            break;
        case 2:
            search_contact_by_name(&user);
            break;
        case 3:
            search_contact_by_index(&user);
            break;
        case 4:
            save_contacts(&user); // Salva os contatos antes de sair
            printf("Saindo...\n");
            break;
        default:
            printf("Opção inválida!\n");
        }
    } while (option != 4);

    return 0;
}

#include <stdio.h>
#include <stdbool.h>

#define MAX_LENGTH 20

int main()
{
    int primes_length;
    printf("How many prime numbers do you want? ");
    scanf("%d", &primes_length);
    int primes[primes_length];
    primes[0] = 2;
    int primes_count = 1;
    bool is_prime = false;

    // Iterate odd numbers
    for (int i = 3; i < primes_length; i += 2)
    {
        // Test divisible by prime numbers
        for (int j = 0; j < primes_count; j++)
        {
            // If the division by primes is not exact once
            // The number is recognized as prime
            int division = i % primes[j];
            if (division == 0)
            {
                is_prime = false;
                break;
            }
            is_prime = true;
        }

        // If the number was recognized as prime it will be added to the primes array
        if (is_prime)
        {
            printf("Number %d is prime\n", i);
            primes[primes_count] = i;
            primes_count++;
            is_prime = false;
        }
    }
    return 0;
}

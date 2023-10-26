import json

def lambda_handler(event, context):
    # Change this to generate primes up to a different limit
    # I've chosen a million
    limit = 1000000  
    prime_numbers = generate_primes(limit)
    # print(prime_numbers)
    if len(prime_numbers) != 0:
        return {
        'statusCode': 200,
        'body': json.dumps('Prime numbers calculated.')
        }

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

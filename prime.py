def generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError("n must be an integer")

    if n == 1:
        return []

    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter a number to find its prime factors: ")
            number = int(user_input)

            if number < 1:
                print("Please enter a positive integer.")
                continue

            prime_factors = generate_prime_factors(number)
            print(f"Prime factors of {number} are: {prime_factors}")
            break  # Exit the loop if input is valid

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

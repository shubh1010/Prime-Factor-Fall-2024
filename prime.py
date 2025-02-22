def generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n == 1:
        return []

    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factorsdef generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
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
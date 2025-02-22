def generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n == 1:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [3]
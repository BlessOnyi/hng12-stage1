import math
import httpx

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d**power for d in digits) == n


fun_fact_cache = {}

async def get_fun_fact(n: int) -> str:
    if n in fun_fact_cache:
        return fun_fact_cache[n]
    url = f"http://numbersapi.com/{n}/math"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            fun_fact_cache[n] = response.text
            return response.text
        return f"No fun fact available for {n}."

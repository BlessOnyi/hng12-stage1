import math
import httpx
import logging


fun_fact_cache = {}

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



async def get_fun_fact(n: int) -> str:
    if n in fun_fact_cache:
        return fun_fact_cache[n]
    
    url = f"http://numbersapi.com/{n}/math"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)
            fun_fact_cache[n] = response.text
            return response.text
        except httpx.HTTPStatusError as e:
            logging.error(f"HTTP error for {n}: {e.response.status_code}")
            return f"No fun fact available for {n}."
        except httpx.RequestError as e:
            logging.error(f"Request error for {n}: {str(e)}")
            return f"Failed to fetch fun fact."


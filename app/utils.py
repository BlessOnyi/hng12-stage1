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
    digits = [int(d) if n < 0 else int(d) for d in str(n)[1:]]
    power = len(digits)
    return sum(d**power for d in digits) == n



async def get_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{n}/math?json=true"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Check for HTTP errors
            return response.json().get("text", "No fun fact available.")
        except httpx.RequestError:
            return "Failed to fetch fun fact."
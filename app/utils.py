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


async def get_fun_fact(n: int) -> str:
    """
    Fetch a mathematical fun fact from Numbers API.
    """
    url = f"http://numbersapi.com/{n}/math"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5)  # Set a timeout for reliability
            response.raise_for_status()  # Ensure the response is valid
            return response.text
    except httpx.HTTPStatusError:
        return f"Could not retrieve a fun fact for {n} (Invalid response)."
    except httpx.RequestError:
        return "Network error: Unable to fetch fun fact."

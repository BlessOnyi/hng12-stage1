from fastapi import FastAPI, HTTPException                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .models import NumberResponse
from .utils import is_prime, is_perfect, is_armstrong, get_fun_fact


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/classify-number")
async def classify_number(number: str = None):
    if not number:
    
        return JSONResponse(
            content={"number": "alphabet", "error": "true"},
            status_code=400
        )
    
    try:
        number = int(number)
    except ValueError:
        return JSONResponse(
            content={"number": "alphabet", "error": "true"},
            status_code=400
        )

    properties = []

    if is_armstrong(number):
        properties.append("armstrong")
    if is_prime(number):
        properties.append("prime")
    if is_perfect(number):
        properties.append("perfect")


    properties.append("odd" if number % 2 else "even")

   
    fun_fact = await get_fun_fact(number)

    digits = [int(d) for d in str(abs(number))]
    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(digits[1:]) - digits[0] if number < 0 else sum(digits), 
        "fun_fact": fun_fact
    }
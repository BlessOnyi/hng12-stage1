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


@app.get("/api/classify-number", response_model=NumberResponse)
async def classify_number(number: str):
    try:
        number = int(number)  # Try converting to int FIRST
    except ValueError:
        return JSONResponse(content={"number": number, "error": True, "message": "Invalid input. Please provide an integer."}, status_code=400)

    if number < 0:  # THEN check if it's negative
        raise HTTPException(status_code=400, detail={"error": True, "number": number, "message": "Negative numbers are not supported."})

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")

    fun_fact = await get_fun_fact(number)


    return NumberResponse(
        number=number,
        is_prime=is_prime(number),
        is_perfect=is_perfect(number),
        properties=properties,
        digit_sum=sum(int(digit) for digit in str(number)),
        fun_fact=fun_fact
    )

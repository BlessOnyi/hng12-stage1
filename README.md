# HNG12 Stage 1 - Number Classification API

## Description

TThis is a RESTful API developed as part of the HNG12 internship Stage 1 task. The API provides an endpoint that classifies a given number based on its mathematical properties and returns a fun fact about it. The API is built with FastAPI for optimal performance and includes proper CORS handling for cross-origin requests.

Key Features:
Classifies numbers as prime, perfect, armstrong, even, or odd
Computes the digit sum of the given number
Fetches a fun fact about the number from the Numbers API
Handles input validation and provides proper error responses
CORS support for cross-origin requests
Fast response time (< 500ms)
Returns responses in JSON format
 

## Technologies Used
- Python  
- FastAPI  
- Uvicorn  
- CORS Middleware  


## CORS Handling
This API allows Cross-Origin Resource Sharing (CORS) to enable frontend applications to access it.
FastAPI's `CORSMiddleware` is used to allow requests from all origins.


## API Specification



### Endpoint
GET http://127.0.0.1:8000//api/classify-number?number=<int>


### Request Examples:
GET http://127.0.0.1:8000/api/classify-number?number=371


### Response Format
The API returns a JSON response with HTTP status code 200 OK:
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request):
```Json
{
  "number": "invalid_input",
  "error": true
}
```

### Response Codes  
- `200 OK` – Request successful  
- `400 Bad Request` - Invalid input(non-integer values)
- `500 Internal Server Error` – Server issue 



## Local Development Setup  
### Prerequisites  
Ensure you have the following installed:  
- Python 3.x  
- pip  

### Steps to Set Up Locally  
1. **Clone the repository:**  
   ```sh
   git clone https://github.com/BlessOnyi/hng12-stage1-api.git
   cd hng12-stage1-api

2. **Create and Activate a Virtual Environment:**  
  python -m venv venv

  **Activate Environment**
- source venv/bin/activate  # On macOS/Linux
- venv\Scripts\activate  # On Windows

3. **Install dependencies**  
   Run the following command to install all required dependencies:
   ```sh
   pip install -r requirements.txt

4. **Run the development server:**
- uvicorn main:app --reload
- The API will be available at: http://127.0.0.1:8000/api/classify-number?number=<your_number>


## Deployment

### To deploy this API using Vercel:
1. **Install Vercel CLI:**  
   ```sh
   npm i -g vercel

2. **Login to Vercel:**  
   ```sh
   vercel login


3. **Deploy to Production:**
   ```sh
   vercel --prod


## Installation
4. **Install dependencies**  
   Ensure you have requirements.txt. If you dont, Run the following command:
   ```sh
   pip install -r requirements.txt

5. **Set the start command**
  uvicorn main:app --host 0.0.0.0 --port $PORT

### Environment Variables  
- `PORT`: Server port (default: 8000)

### The API is deployed at: 


### Testing
1. **Using Postman:**

- Open Postman
- Create a new GET request
- Enter the URL: Deployed API URL
- Send the request
- Verify the JSON response matches the specified format

2. **Performance:**
- Response time: < 500ms
- Monitored using Vercel Analytics
- Optimized for quick response through FastAPI's async capabilities


### Additional Resources
🔗 Numbers API
🔗 Parity in Mathematics


### Backlink related to my chosen programming language/stack:
[Hire Python Developers](https://hng.tech/hire/python-developers)







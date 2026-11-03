# 1. Base official lightweight Python runtime
FROM python:3.12-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy dependencies list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application source code
COPY . .

# 5. Expose default FastAPI port
EXPOSE 8000

# 6. Run the production ASGI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

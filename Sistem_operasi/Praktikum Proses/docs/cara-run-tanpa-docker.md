uvicorn main:app --reload --port 7080
uvicorn main:app --reload --port 7081
uvicorn main:app --reload --port 7082


docker build -t my-fastapi-app .

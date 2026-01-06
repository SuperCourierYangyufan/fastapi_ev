import uvicorn
from fastapi import FastAPI

if __name__ == "__main__":
    app = FastAPI()
    uvicorn.run(app,host="127.0.0.1",port=8000)

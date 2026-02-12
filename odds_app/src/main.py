import uvicorn
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def central_function():
    run()
    return {"Neural": "Nine"}

def run():
    os.system("python -m pet_herding")
    



if __name__ == "__main__":
    #run()
    uvicorn.run(app, port=8000, host="0.0.0.0")
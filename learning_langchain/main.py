import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from learning_langchain.routers import talk_spark
import uvicorn


load_dotenv()

app = FastAPI()

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(
    talk_spark.router,
    prefix="/talk_spark",
    tags=["talk_spark"],
)

PORT = int(os.get("PORT", 8000))
HOST = "0.0.0.0"

if __name__ == "__main__":
    uvicorn.run("learning_langchain.main:app", host=HOST, port=PORT, reload=True)

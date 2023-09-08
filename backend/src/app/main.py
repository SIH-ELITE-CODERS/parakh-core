from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Alive and Kickin!"}

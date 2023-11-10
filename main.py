from fastapi import FastAPI

app = FastAPI()

@app.get("/celsius_degrees/{celsius}")
async def converter(celsius:float):
    fahrenheit = 9 / 5 * celsius + 32
    return {'градусы по шкале Фаренгейта':fahrenheit}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
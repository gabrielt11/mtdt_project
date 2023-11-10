from fastapi import FastAPI

app = FastAPI()

@app.get("/celcius_degrees/{celcius}")
async def converter(celcius:float):
    farenheit = 9 / 5 * celcius + 32
    return {'градусы по шкале Фаренгейта':farenheit}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
import asyncio
import websockets
from websockets import ServerConnection
import random

time = random.uniform(1.0, 2.0)

req = ["Привет", "Пока", "Алоха"]
res_on = ["Инициализация...", "Пользователь подтверждён...", "Добрый день!", "Ты сегодня хорошо выглядишь!", "Как и всегда ^_^"]
res_off = ["Инициализация...", "Попытка 2...", "Попытка 3...", "Ошибка авторизации пользователя!", "Обратитесь за уточнением к администратору за уточнением"]
count = 0

# Обработка входящих сообщений
async def echo(websocket: ServerConnection):
    global count
    async for message in websocket:
        print(f"Сообщение от пользователя {message}")
        if message in req:
            for i in res_on:
                await asyncio.sleep(time)
                count += 1
                response = f"{count}. {i}"
                await websocket.send(response)
        else:
            for i in res_off:
                await asyncio.sleep(time)
                count += 1
                response = f"{count}. {i}"
                await websocket.send(response)
        count = 0


# Запустк сервера
async def main():
    server = await websockets.serve(echo, 'localhost', 8765)
    print("Server started on ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())
import asyncio
import websockets


async def client():
    uri = "ws://localhost:8765"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Привет"  # Сообщение, которое отправит клиент
        print(f"Отправка: {message}")
        await websocket.send(message)  # Отправляем сообщение

        while True:
            try:
                response = await asyncio.wait_for(websocket.recv(), timeout=3.0)
                print(f"Ответ от сервера: {response}")
            except:
                break

        response = await websocket.recv()  # Получаем ответ от сервера
        print(f"Ответ от сервера: {response}")


asyncio.run(client())

import asyncio
async def fetch_data(id):
    print(f"Начинаем загрузку данных {id}")
    await asyncio.sleep(2)
    print(f"Данные {id} загружены")
    return f"Результат {id}"

async def main():
    task1=asyncio.create_task(fetch_data(1))
    task2=asyncio.create_task(fetch_data(2))
print("Задачи запущены")
result1=await.task1
result2=await.task2
print(f"Получены результаты: {result1}, {result2}")
asyncio.run(main)
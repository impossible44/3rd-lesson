"""result=db.query("Долгий SQL запрос")
result=await db.query("Долгий SQL")
EventLoop(Один поток)

Задача А: запрос к БД - await
Задача Б: запрос к API - await
Задача В: чтение файла - await
Задача А: данные пришли
Задача Б: данные пришли"""


import asyncio

async def task(name, delay):
    print(f'[{name}] начал работу')
    await asyncio.sleep(delay)
    print(f'[{name}] закончил работу')
    
async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 5)
        )
asyncio.run(main())
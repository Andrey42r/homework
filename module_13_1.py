import asyncio

async def start_strongman(name, power):
    for i in range(1, 6):
        print(f'Силач {name} начал соревнования')
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {i} шар')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())

import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} started fetching data")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"this is sample data from {id}"}

async def main():
    results = []

    async with asyncio.TaskGroup() as tg:# with keh sath hamne async kah context manger use kara hai joh lock karega thread execute karega hamri functionality and unlock karderga thread koh 
        # asyncio.TaskGroup() ek alternative hai asyncio.genrator()function kah joh agar ek task fail hota hai toh saare task keh execution stop kardega and hame exception create kardega
        for i, sleep_time in enumerate([1, 2, 3], start=1):# enumeratee ek list of tuple convert karke deta hai iteratable methods keh
            task = tg.create_task(fetch_data(i, sleep_time))
            results.append(task)

    # TaskGroup se bahar – sab tasks complete ho chuke hain
    for task in results:
        print(f"Received result: {task.result()}")

asyncio.run(main())

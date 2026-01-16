import asyncio
import time
async def fetch_data(id,sleep_time):
    print(f"Courutine {id} is starting to fetch data")
    await asyncio.sleep(sleep_time)
    return{"id":id,"data":f"Sample data from Courutine id:{id}"}

async def main():
    results = await asyncio.gather(fetch_data(1,2),fetch_data(2,4),fetch_data(3,2))# asyncio.gather ek quick way hai to run multiple coruntine concurently(sath sath meh) and await ineh sabh coruntines keh finish hone kah wait karega to finish concurently joh gather karega and inke result koh ek list meh store karvadega
    #asyncio.gather error handling keh maalme meh itna acha nahi hai agar koi ek corutine fail hojata hai toh yeh uske karan rukega nahi balki baki keh corutine execute karna shuru kardega
    start_time = time.time()
    for result in results:
        print(f"Recieved results :{result}")
    end_time= time.time()
    print(f"time taken for completion of the function is {end_time-start_time}")

asyncio.run(main())
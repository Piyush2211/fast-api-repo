import asyncio 

async def fetch_data(id,sleep_time):
    print(f"Courutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return{"id":id,"data":f"Sample data from courutine {id}"}

async def main():
    task_1 = asyncio.create_task(fetch_data(1,1))# toh in await hamne dekha tha keh  ham sirf wait kar rahe theh ek corutine keh execute hone kah then humne second courutine execute kiya tha because jabh first khatam hua tha tabh second corutine await hua tha basically start hua but task meh esah nahi hota jaise hi koi corutine sleep hojata hai basically wait kar raha hota hai kise call keh liye joh hamare program keh control meh nahi hai ham move kar sakte hai next task par and useh execute karna start kar sakte hai
    task_2 = asyncio.create_task(fetch_data(2,3))
    task_3 = asyncio.create_task(fetch_data(3,1))
    result_1 = await task_1#but hame ineh tasks keh execution khatam hone kah wait karna padega joh keh 3 second meh hojayegi rather than taking whole 6 second koh keh single single await seh hota rather than creating the task 
    result_2 = await task_2
    result_3 = await task_3 
    #basically when we create a task we are scheduling multiple corutines to work simaltanously as soon as one corutine goes to sleep the second corutine start executing decreasing the execution time
    #basically in order to wait for some specific task to finish than executing the second task all we need to do is move the await task_that_we_need_to_wait before creation of the task which we want to perform   
    print(result_1,result_2,result_3)

asyncio.run(main())
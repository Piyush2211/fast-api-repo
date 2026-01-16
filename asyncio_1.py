# tranditional programing meh hum ek single line by line statements koh execute karte hai par  par asynchronus programming meh hum multiple points seh execute kar sakte hai apne program keh statement koh
# asynico is good for the task which wait alot such as waiting for internet response , or reading a file , threads are good for  task which wait for some task but also share some data which helps them to run in parellel these are good for task which are i o bound and less cpu intensive, So CPU intensive task the processes are the way to go
# har ek process independently perform karta hai maximizing the CPU usage by running in parllel accross multiple cohorts
# event loop is the core that manges and distributes task har task  centre of the loop aata hai for execution agar yeh kiseh keh wait karta hai toh pause kardiya jaata hai and vo task kise aur task koh run hone keh liye space deh deta hai yeh ensure karta hai ki eventloop hamesha efficent rahe jaise hi awaited operation paused task meh pura hoga vo wapis event loop keh centre meh aajayega and execute kardiya jayega
#jabh bhi async programming karenge python meh hum asyncio import karenge 
import asyncio 

#this is a couroutine function
async def fetch_data(delay,id):
    print("fetching data....id:",id)
    await asyncio.sleep(delay)# await can be only utilized inside of a corutine function 

    print("data fetched...id:",id)
    return {"data":"somedata",
            "id":id}

async def main():

    print("start of the main coruntine")
    task_1 = fetch_data(2,1)
    task_2= fetch_data(2,2)
    print("end of corutine")
    result_1= await task_1# ek corutine tabh tak execute hona start nahi hota jabh tak voh await nahi kara jata hai yah vo kese task meh wrap nah kara jaye 
    print(f"Recived Result:{result_1}")
    result_2 = await task_2
    print(f"Recived Result: {result_2}")
    
# yeh jabh execute hoga toh hame ek Courutine object return karega main()-> Corutine object
print(main())
asyncio.run(main())# basically asyncio.run await karta hai main() keh liye joh ek corutine object hai thats why we  use it
#main() joh keh hamra corutine object hai usko hum asyncio.run meh pass karenge yeh hamara corutine execute karega and then event loop koh start kardega   and asyncronus code run karega
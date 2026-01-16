import asyncio  # asyncio module import kar rahe hain (async programming ke liye)

# Ye async function future ke andar result set karega
async def set_future_result(future, value):
    
    # 2 seconds ka non-blocking wait
    # Is dauran event loop free rehta hai
    await asyncio.sleep(2)
    
    # Future ke andar result set kar diya
    # Jaise hi ye execute hota hai, future "complete" ho jata hai
    future.set_result(value)
    
    # Confirmation ke liye print
    print(f"set the future result to {value}")

# Main async function jahan se program start hota hai
async def main():
    
    # Current running event loop ko access kar rahe hain
    loop = asyncio.get_running_loop()
    
    # Event loop se ek empty future create kiya
    # Abhi isme koi result nahi hai
    future = loop.create_future()
    
    # set_future_result() ko background me run kar rahe hain
    # Ye function 2 seconds baad future ka result set karega
    asyncio.create_task(
        set_future_result(future, "future results are ready")
    )
    
    # Yahan main() pause ho jaata hai
    # Jab tak future ka result set nahi hota
    result = await future
    
    # Jaise hi future complete hota hai, ye line execute hoti hai
    print(f"Recieved the future results: {result}")

# Event loop start karta hai aur main() ko run karta hai
asyncio.run(main())

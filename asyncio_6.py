import asyncio

# Shared resource jo multiple async tasks use karenge
shared_resource = 0

# Async lock create kiya
# Yeh ensure karega ki ek time par sirf ek task
# shared_resource ko modify kare
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource  # Global variable ko modify karne ke liye

    # Lock acquire hoga yahan
    # Jab tak yeh block complete nahi hota,
    # koi aur task is resource ko access nahi kar sakta
    async with lock:
        # Modification se pehle value print
        print(f"Resource before modification : {shared_resource}")

        # Shared resource ko safely increment kar rahe hain
        shared_resource += 1

        # Artificial delay
        # Context switch ho sakta hai yahan,
        # lekin lock ki wajah se race condition nahi hogi
        await asyncio.sleep(1)

        # Modification ke baad value print
        print(f"Resource after modification: {shared_resource}")

    # Yahan aate hi lock automatically release ho jaata hai

async def main():
    # modify_shared_resource ko 5 baar parallel run kar rahe hain
    # asyncio.gather sabhi tasks ko ek saath start karta hai
    await asyncio.gather(
        *(modify_shared_resource() for task in range(5))
    )

# Event loop start hota hai yahan se
# main() async function ko run karta hai
asyncio.run(main())

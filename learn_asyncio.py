# using async io we can write concurrent execution code via async/await syntax.  
# In synchronous code execution, a function is executed one after another function is already executed.
# In asynchronous code execution, another function execution can start while the previous one is waiting for data from internet or IO operation. 
# Asyncio doesn't means fast but executing other tasks while the older one is waiting for internet download or IO tasks, better then to sit idle.
# It is single threaded and runs on a single process. Runs on a single processor and follows co-operative multiple tasking where processes give up control voluntarily.
import asyncio
import time
# from datetime import datetime

# synchronous function: They do not have the ability to yield the control over and take back later.
def sync_func(arg: str) -> None:
    print("started function execution for sync_func", arg) 
    time.sleep(2)
    print("Finished function execution for sync_func", arg) 

def sync_func2(arg: str) -> None:
    print("started function execution for sync_func2", arg) 
    time.sleep(2)
    print("Finished function execution for sync_func2", arg) 

async def async_func(arg: str) -> None:
    print("Started function exexcution for async_func", arg)
    # time.sleep(2)
    await asyncio.sleep(2)
    print("Finished function execution for async_func", arg) 
    
async def async_func2(arg: str) -> None:
    print("Started function exexcution for async_func2", arg)
    # time.sleep(2)
    await asyncio.sleep(2)
    print("Finished function execution for async_func2", arg)

async def main():
    start_time = time.time()
    print("Calling function sync_func")
    sync_func("Check....")
    print("Back to main function")

    print("Calling function sync_func2")
    sync_func2("Check2....")
    print("Back to main function2")
    print(f"Total time taken {time.time()-start_time}")

    print("--------------------------------------------")

    # Await keyword should be used within async function
    # Await can be used only with asynchronous function reason being synchronous functions are not aware on how to pass the control to event loop and resume later.
    # Await keyword tells the event loop to take back control from currently executed function and give it to some other function for execution. Awaitable task will remain suspended until that task io or other dependent tasks complete.
    # Types of awaitable objects: 
        # Co-routines: Created when async functions are called. Coroutine functions are also know as async function and coroutine objects are also created when coroutine functions are called. Need to await the coroutine object to execute the same coroutine functions.
    start_time = time.time()
    print("Calling function async_func")
    await async_func("Check async....")
    print("Back to main function async_func")

    print("Calling function async_func2")
    await async_func2("Check2 async....")
    print("Back to main function async_func2")
    print(f"Total time taken {time.time()-start_time}")


    print("--------------------------------------------")
        # tasks: wrappers around co-routines that can be executed independently. When coroutine is wrapped in a task it gets handed over event loop to execute whenever it gets a chance.
        # Follows FIFO, like the one created earliest will be executed first otherwise the one which is available for execution.
    start_time = time.time()  
    async_task1 = asyncio.create_task(async_func("Check async...."))
    async_task2 = asyncio.create_task(async_func2("Check async2...."))
    await async_task1
    await async_task2
    print(f"Total time taken {time.time()-start_time}")
    print("---- Execution 2nd Time ----")
    start_time = time.time()  
    async_task2 = asyncio.create_task(async_func2("Check async2...."))
    async_task1 = asyncio.create_task(async_func("Check async...."))
    await async_task1
    await async_task2
    print(f"Total time taken {time.time()-start_time}")


    print("--------------------------------------------")

    # futures: low level object representing result. 

    # in case the code doesn't contains asynchronous features, we can wrap them in threads or processes to have the asynchronous feature.
    print("Thread execution started")
    start_time = time.time()
    thread_async_task1 = asyncio.create_task(asyncio.to_thread(sync_func, 1))
    thread_async_task2 = asyncio.create_task(asyncio.to_thread(sync_func, 2))
    res1 = await thread_async_task1
    print("Thread 1 fully completed....")
    res2 = await thread_async_task2
    print("Thread 2 fully completed....")
    print(f"Total time taken {time.time()-start_time}")


if __name__ == "__main__":
    # In order to run asyncio function, need to start event loop first. Event loop can be imagined as a scheduler which takes into account of all the tasks needed to be executed, it passes or gives the control to different tasks or functions.
    asyncio.run(main())


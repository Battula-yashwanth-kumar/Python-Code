import time
import asyncio
import requests

async def function1():
    print("func 1")
    url="https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response=requests.get(url)
    open("instagram.jpg","wb").write(response.content)
    return "Hello"

async def function2():
    print("func 2")
    url="https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    response=requests.get(url)
    open("instagram.jpg","wb").write(response.content)

async def function3():
    print("func 3")
    url="https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response=requests.get(url)
    open("instgram3.ico","wb").write(response.content)


async def main():
    # await function1()  # await make the function to wait and make the functions to run one after the another
    # await function2()
    # await function3()


    # L = asyncio.create_task(function1()) # when every this function gets time i t will run
    # await function2()
    # await function3()

    L= await asyncio.gather(    # It will make sure that all the functions will run simultaneously (concurrently)
        function1(),
        function2(),
        function3(),
    )

asyncio.run (main())




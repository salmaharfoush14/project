import asyncio
from websockets.asyncio.client import connect

async def main():
    async with connect("ws://localhost:8765") as ws:
        await ws.send("Hello!")
        reply = await ws.recv()
        print("Got back:", reply)
        
asyncio.run(main())
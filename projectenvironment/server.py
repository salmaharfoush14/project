import asyncio
from websockets.asyncio.server import serve

async def handler(ws):
    async for message in ws:
        await ws.send(message)
        
async def main():
    async with serve(handler, "localhost", 8765):
        print("Server running on port 8765")
        await asyncio.Future()
        
asyncio.run(main())

        
    
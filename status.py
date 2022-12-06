import rpc
import time
import asyncio
import windowUtils
from time import mktime

client_id = '1049193773982302240'  # Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

start_time = mktime(time.localtime())
bigText = "I am currently"
smallText = "testing my custom rpc"
hardcodedGamesList = ["Deep Rock Galactic"]


async def activity():
    activity = dict(state=smallText, details=bigText, timestamps={
        "start": start_time
    }, assets={
        "small_text": "image by nanbou",  # anything you like
        "small_image": "pinhead_nanbou",  # must match the image key
        "large_text": "image by pachikko",  # anything you like
        "large_image": "pinhead_pachi"  # must match the image key
    })
    rpc_obj.set_activity(activity)
    await asyncio.sleep(5)


async def windowCheck():
    fullscreenApp = windowUtils.findFullscreenApp()
    if fullscreenApp:
        bigText = "Playing a Game"
        smallText = fullscreenApp
    else:
        window = windowUtils.getFocusedWindow()
        bigText = "Playing a Game"
        smallText = window

    # Messy way
    # runningApps = windowUtils.getWindows()
    # for window in runningApps:
    #     if window in hardcodedGamesList:
    #         bigText = "Playing a Game"
    #         smallText = window
    await asyncio.sleep(10)


async def main():
    await activity()
    await windowCheck()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

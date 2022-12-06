import rpc
import time
import signal
import asyncio
import warnings
import windowUtils
from time import mktime

warnings.filterwarnings("ignore", category=DeprecationWarning) # Prevents 3.10 from complaining about asyncio.ensure_future(activity())
client_id = '1049193773982302240'  # Your application's client ID, this is what will display as your rpc's game
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

start_time = mktime(time.localtime())


async def activity():
    while True:
        detailsText, stateText = await windowCheck()
        activity = dict(state=stateText, details=detailsText, timestamps={
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
    window = windowUtils.getFocusedWindow()
    print(fullscreenApp)
    print(window)
    if fullscreenApp:
        detailsText = "Playing a Game"
        stateText = fullscreenApp
    elif window:
        detailsText = "Playing a Game"
        stateText = window
    else:
        detailsText = "I am currently"
        stateText = "using my custom rpc"
    return detailsText, stateText


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop) # Avoids errors in 3.11
    asyncio.ensure_future(activity())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.stop()

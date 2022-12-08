import rpc
import time
import asyncio
import warnings
import windowUtils
from time import mktime


# Change these
client_id = '1049193773982302240'  # Your application's client ID, this is what will display as your rpc's game
gamesList = ["Team Fortress 2", "Deep Rock Galactic", "Risk of Rain 2", "Roblox", "Satisfactory"]  # Window names registered as games
toolsList = ["Blender", "Source Filmmaker", "PyCharm"]  # Window names registered as tools/apps
defaultDetails = "I am currently:"  # Default text for no game/tool
defaultState = "being a wee bit silly"  # Second line of default text
defaultGame = "Killing enemy gamers in "  # Default text for playing a game
defaultTool = "Working hard in "  # Default text for using a tool


playingWindow = None
detailsText = None
stateText = None



warnings.filterwarnings("ignore", category=DeprecationWarning)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
print("RPC connection successful.")

start_time = mktime(time.localtime())


async def activity():
    global detailsText
    global stateText
    while True:
        await windowCheck()
        activity = dict(state=stateText, details=detailsText, timestamps={
            "start": start_time
        }, assets={
            "small_text": "image by nanbou",  # anything you like
            "small_image": "pinhead_nanbou",  # must match the image key
            "large_text": "image by pachikko",  # anything you like
            "large_image": "pinhead_pachi"  # must match the image key
        })
        rpc_obj.set_activity(activity)
        await asyncio.sleep(10)
        print("Hi")


async def windowCheck():
    global playingWindow  # This part can probably be cut down but IDK man
    global detailsText
    global stateText
    runningApps = windowUtils.getWindows()

    if playingWindow is None:
        for window in runningApps:
            if window in gamesList:
                detailsText = defaultGame
            elif window in toolsList:
                detailsText = defaultTool
            stateText = playingWindow = window  # Override both at once for efficiency
    else:
        if playingWindow not in runningApps:  # Set back to defaults
            playingWindow = None
            detailsText = defaultDetails
            stateText = defaultState
    return


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(activity())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        if not task.cancelled():
            print("Shutting down RPC.")
            task.cancel()
        else:
            task = None

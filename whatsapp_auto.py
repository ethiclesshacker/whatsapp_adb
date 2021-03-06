from ppadb.client import Client as AdbClient
import time

# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.devices()[0]

# Launch whatsapp using adb
device.shell("am start -n com.whatsapp/com.whatsapp.Main")

position = 670
count = 0
for i in range(8):
    print(i+1)
    while(position <= 2250):
        # Press new message
        device.shell("input touchscreen tap 1000 2200")

        for _ in range(i):
            # Scroll the screen by screen height amount (or a little less).
            # Scrolling i times because i number of screens have already been done.
            device.shell("input touchscreen swipe 500 2200 500 200 2000")

            # Tuning left.

        # Select chat
        device.shell(f"input touchscreen tap 500 {position}")
        
        # Position for next chat
        position += 170

        # Sleep to be replaced with actions for each chat.
        time.sleep(0.5)

        # Press the back button to exit from chat window
        device.shell("input keyevent 4")

    # First screen != rest screens.
    # Resetting position for next page
    position = 300


def sendMessage(message):
    device.shell('input text "'+message+'"')

    # Keyevent 66 - ENTER key
    device.shell("input keyevent 66")

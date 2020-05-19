from ppadb.client import Client as AdbClient
import time

# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.devices()[0]

# Launch whatsapp using adb
device.shell("am start -n com.whatsapp/com.whatsapp.Main")

# Opens New messagw window directly
device.shell("am start -n com.whatsapp/com.whatsapp.ContactPicker")

# Long press on 1st contact to activate select mode in new message window.
device.shell("input touchscreen swipe 500 670 500 670 3000")

# Select all other chats
# Range unknown
position = 850
for i in range(8):
    print(i+1)
    while(position <= 2250):
        device.shell(f"input touchscreen tap 500 {position}")
        position += 170
        time.sleep(0.5)

    device.shell("input touchscreen swipe 500 2200 500 200 2000")
    position = 300


def sendMessage(message):
    device.shell('input text "'+message+'"')
    
    # Keyevent 66 - ENTER key
    device.shell("input keyevent 66")
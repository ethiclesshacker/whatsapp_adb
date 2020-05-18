from ppadb.client import Client as AdbClient
# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.devices()[0]

device.shell("input touchscreen swipe 400 400 400 700 400")
device.shell("input touchscreen swipe 400 400 700 400 400")
device.shell("input touchscreen swipe 700 400 700 700 400")
device.shell("input touchscreen swipe 400 700 700 700 400")
device.shell("input touchscreen swipe 400 700 700 400 400")
device.shell("input touchscreen swipe 400 400 700 700 400")

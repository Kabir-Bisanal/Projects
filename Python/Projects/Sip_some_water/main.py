import time
from plyer import notification
while True:
    print("Please sip some water!!")
    notification.notify(title="WATER", message="You need to sip some water ASAP!!")
    time.sleep(60*60)
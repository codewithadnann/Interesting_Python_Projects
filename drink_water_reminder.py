import time
from plyer import notification

def drink_water_reminder():
    notification.notify(
        title="💧 Drink Water",
        message="Time to hydrate! 🥤",
        timeout=10  # seconds
    )

while True:
    drink_water_reminder()
    time.sleep(100)  # Every 100 seconds (for testing)

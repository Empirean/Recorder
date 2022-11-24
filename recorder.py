from time import time
from tkinter import EventType
from pynput import keyboard, mouse
import json
import os

class Recorder:
    unreleased_keys = []
    input_event = []
    mouse_listener = None
    start_time = 0.0

    class EventType:
        KEYDOWN = "keyDown"
        KEYUP = "keyUp"
        CLICK = "click"

    def __init__(self, filename):
        # Mouse listener
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.mouse_listener.start()
        self.mouse_listener.wait()

        # Keyboard listener
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
                self.start_time = time()
                listener.join()
            
        print(f"Recording duration {self.time_elapsed()}")
        # print(json.dumps(self.input_event, indent=4))

        script_dir = os.path.dirname(__file__)
        filepath = os.path.join(script_dir, "recordings", f"{filename}.json")

        with open(filepath, "w") as outfile:
            json.dump(self.input_event, outfile, indent=4)

    def record_event(self, event_type, event_time, button, pos=None):
        self.input_event.append({
            "time" : event_time,
            "type" : event_type,
            "button" : str(button),
            "pos" : pos
        })

        if event_type == self.EventType.CLICK:
            print(f"{event_type} on {button} pos {pos} at {event_time}")
        else:
            print(f"{event_type} on {button} at {event_time}")
        

    # Mouse listener functions
    def on_click(self, x, y, button, pressed):
        if not pressed:
            self.record_event(self.EventType.CLICK, self.time_elapsed(), button, (x,y))

    # Keyboard listener fuctions
    def on_press(self, key):
        # inhibits multiple press calls when holding a key
        if key in self.unreleased_keys:
            return
        else:
            self.unreleased_keys.append(key)

        # actual key press    
        try:
            self.record_event(self.EventType.KEYDOWN, self.time_elapsed(), key.char)
        except AttributeError:
            self.record_event(self.EventType.KEYDOWN, self.time_elapsed(), key)

    def on_release(self, key):
        # inhibits multiple press calls when holding a key
        try:
            self.unreleased_keys.remove(key)
        except ValueError:
            print(f"Error: {key} not an unreleased key")

        # actual key release
        try:
            self.record_event(self.EventType.KEYUP, self.time_elapsed(), key.char)
        except AttributeError:
            self.record_event(self.EventType.KEYUP, self.time_elapsed(), key)

        if key == keyboard.Key.esc:
            # Stop listener
            self.mouse_listener.stop()

            return False      

    def time_elapsed(self):
        return time() - self.start_time
    
    
    
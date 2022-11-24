import pyautogui
from time import sleep, time
import os
import json

class Playback:

    def __init__(self, filename):
        pyautogui.FAILSAFE=True
        self.countdown_timer()
        self.play_actions(filename=filename)

    def play_actions(self, filename):
        
        script_dir = os.path.dirname(__file__)
        filepath = os.path.join(
            script_dir,
            "recordings",
            filename
        )

        with open(filepath, "r") as jsonfile:
            data = json.load(jsonfile)
            
            for index, action in enumerate(data):
                action_start_time = time()

                if action["button"] == "Key.esc":
                    break

                if action["type"] == "keyDown":
                    key = self.convertKey(key)
                    pyautogui.keyDown(key)
                    print(f"keyDown on {key}")
                elif action["type"] == "keyUp":
                    key = self.convertKey(key)
                    pyautogui.keyUp(key)
                    print(f"keyUp on {key}")
                elif action["type"] == "click":
                    pyautogui.click(action["pos"][0], action["pos"][1], duration=0.25)
                    print(f"click on {action['pos']}")

                try:
                    next_action = data[index + 1]
                except IndexError:
                    break
            
                elapsed_time = next_action["time"] - action["time"]

                if elapsed_time < 0:
                    raise Exception("Unexpected action ordering.")

                elapsed_time -= (time() - action_start_time)
                if elapsed_time < 0:
                    elapsed_time = 0
                
                print(f"sleeping for {elapsed_time}")
                sleep(elapsed_time)

    def convertKey(self, button):
        PYNPUT_SPECIAL_CASE_MAP = {
            'alt_l': 'altleft',
            'alt_r': 'altright',
            'alt_gr': 'altright',
            'caps_lock': 'capslock',
            'ctrl_l': 'ctrlleft',
            'ctrl_r': 'ctrlright',
            'page_down': 'pagedown',
            'page_up': 'pageup',
            'shift_l': 'shiftleft',
            'shift_r': 'shiftright',
            'num_lock': 'numlock',
            'print_screen': 'printscreen',
            'scroll_lock': 'scrolllock',
        }

        cleaned_key = button.replace("Key.", "")

        if cleaned_key in PYNPUT_SPECIAL_CASE_MAP:
            return PYNPUT_SPECIAL_CASE_MAP[cleaned_key]

        return cleaned_key

    def countdown_timer(self):
        # Countdown timer
        print("Starting", end="", flush=True)
        for i in range(0, 10):
            print(".", end="", flush=True)
            sleep(1)
        print("Go")
        
                
                    